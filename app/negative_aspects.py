from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

class ReviewAnalyzer:
    def __init__(self):
        # Initialize models
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.themes = ["Gameplay", "Visuals", "Performance", "Sound", "Story", "Controls", "Difficulty", "Replayability"]

    def analyze_review(self, review):
        # Split sentences and get the embeddings
        sentences = review.split('.')
        sentence_embeddings = self.embedding_model.encode(sentences)
        theme_embeddings = self.embedding_model.encode(self.themes)

        # Match themes to each sentence
        relevant_themes = {theme: [] for theme in self.themes}
        for i, sentence_embedding in enumerate(sentence_embeddings):
            similarities = util.cos_sim(sentence_embedding, theme_embeddings)
            best_theme_idx = similarities.argmax()
            relevant_themes[self.themes[best_theme_idx]].append(sentences[i])

        # Analyze sentiment for sentences in each theme
        results = {}
        for theme, sentences in relevant_themes.items():
            sentiments = self.sentiment_pipeline(sentences)
            results[theme] = [(sentence, sentiment['label']) for sentence, sentiment in zip(sentences, sentiments)]

        # Count positive and negative sentiments for each theme
        negative_themes = {}
        for theme, sentiments in results.items():
            positive_count = sum(1 for _, sentiment in sentiments if sentiment == 'POSITIVE')
            negative_count = sum(1 for _, sentiment in sentiments if sentiment == 'NEGATIVE')
            if negative_count > positive_count:
                negative_themes[theme] = sentiments

        return [theme for theme in negative_themes]
