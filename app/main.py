from negative_aspects import ReviewAnalyzer
from recommended import ReviewClassifier

import tkinter as tk
from tkinter import ttk, filedialog
import threading
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    aspects_analyzer = None
    review_classifier = None

    # Create the window
    root = tk.Tk()
    root.title("Game Review Analyzer")

    # Create a frame
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    # Label to show loading status
    loading_label = ttk.Label(frame, text="Initializing...")
    loading_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))


    def initialize_classes():
        nonlocal aspects_analyzer, review_classifier
        aspects_analyzer = ReviewAnalyzer()
        review_classifier = ReviewClassifier()
        loading_label.config(text="Initialization complete")
        time.sleep(1)  # Give a moment to show the completion message
        loading_label.grid_forget()
        display_main_ui()

    def display_main_ui():
        notebook = ttk.Notebook(frame)
        notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        manual_frame = ttk.Frame(notebook, padding="10")
        manual_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        manual_frame.columnconfigure(0, weight=1)
        notebook.add(manual_frame, text="Manual Review Analysis")

        review_label = ttk.Label(manual_frame, text="Enter a game review:")
        review_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        review_text = tk.Text(manual_frame, width=50, height=10, wrap=tk.WORD)
        review_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        analyze_button = ttk.Button(manual_frame, text="Analyze")
        analyze_button.grid(row=2, column=0, sticky=tk.W, pady=(0, 10))

        recommendation_label = ttk.Label(manual_frame, text="Recommendation: ")
        recommendation_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))

        negative_aspects_label = ttk.Label(manual_frame, text="Negative Aspects: ")
        negative_aspects_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))

        def run_analysis():
            review = review_text.get("1.0", tk.END).strip()
            if review.lower() == 'exit':
                root.destroy()
                return

            def analyze():
                recommendation = review_classifier.predict(review)
                negative_aspects = aspects_analyzer.analyze_review(review)
                return recommendation, negative_aspects

            recommendation, negative_aspects = analyze()
            recommendation_label.config(text=f"Recommendation: {recommendation}")
            negative_aspects_label.config(text=f"Negative Aspects: {negative_aspects}")

        analyze_button.config(command=lambda: threading.Thread(target=run_analysis).start())
        analyze_button.config(state=tk.NORMAL)

        csv_frame = ttk.Frame(notebook, padding="10")
        csv_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        csv_frame.columnconfigure(0, weight=1)
        notebook.add(csv_frame, text="CSV Review Analysis")

        open_file_button = ttk.Button(csv_frame, text="Open CSV File")
        open_file_button.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        file_name_label = ttk.Label(csv_frame, text="No file selected")
        file_name_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))

        analyze_csv_button = ttk.Button(csv_frame, text="Analyze CSV", state=tk.DISABLED)
        analyze_csv_button.grid(row=0, column=2, sticky=tk.W, padx=(10, 0))

        def open_file():
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if file_path:
                file_name_label.config(text=file_path.split('/')[-1])
            analyze_csv_button.config(state=tk.NORMAL)
            analyze_csv_button.config(command=lambda: analyze_csv_reviews(file_path))

        open_file_button.config(command=open_file)

        csv_result_label = ttk.Label(csv_frame, text="CSV Analysis Result: ")
        csv_result_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))

        def analyze_csv_reviews(file_path):
            df = pd.read_csv(file_path)
            print(df)
            reviews = df['reviews'].tolist()

            recommendations = []
            negative_aspects_count = {}

            for review in reviews:
                recommendation = review_classifier.predict(review)
                recommendations.append(recommendation)

                negative_aspects = aspects_analyzer.analyze_review(review)
                for aspect in negative_aspects:
                    if aspect in negative_aspects_count:
                        negative_aspects_count[aspect] += 1
                    else:
                        negative_aspects_count[aspect] = 1

            recommended_count = recommendations.count('Recommended')
            total_reviews = len(reviews)

            result_text = (f"Recommended: {recommended_count / total_reviews * 100:.2f}%\n")
            csv_result_label.config(text=f"CSV Analysis Result:\n{result_text}")

            fig, ax = plt.subplots()
            ax.bar(negative_aspects_count.keys(), negative_aspects_count.values())
            ax.set_xlabel('Negative Aspects')
            ax.set_ylabel('Count')
            ax.set_title('Negative Aspects Frequency')
            tick_positions = range(len(negative_aspects_count)) 
            tick_labels = list(negative_aspects_count.keys())
            ax.set_xticks(tick_positions)
            ax.set_xticklabels(tick_labels, rotation=45, ha='right')

            fig.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=csv_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

    init_thread = threading.Thread(target=initialize_classes)
    init_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
