import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import jsonlines
import pickle
import os

class ReviewClassifier:
    def __init__(self, model_path='model.pkl', vectorizer_path='vectorizer.pkl'):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path

        if not os.path.exists(self.model_path) or not os.path.exists(self.vectorizer_path):
            self.train_model()
        else:
            self.load_model()

    def train_model(self):
        exampleData = {"review": None, "rating": None}

        files = [
            r'C:\Users\olive\Coding\Kiu\Code\data\Counter_Strike_Global_Offensive.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Counter_Strike.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Dota_2.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Football_Manager_2015.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Garrys_Mod.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Grand_Theft_Auto_V.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Sid_Meiers_Civilization_5.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Team_Fortress_2.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\The_Elder_Scrolls_V.jsonlines',
            r'C:\Users\olive\Coding\Kiu\Code\data\Warframe.jsonlines'
        ]

        data = []

        # Append data from other jsonlines files
        for file in files:
            with jsonlines.open(file) as reader:
                data2 = [{k: obj[k] for k in exampleData if k in obj} for obj in reader]
                data.extend(data2)

        # Transform to DataFrame
        df = pd.DataFrame(data)

        # create the balanced dataframe 
        balanced_df = pd.concat([df[df['rating'] == 'Recommended'].sample(10000, random_state=42),
                                 df[df['rating'] == 'Not Recommended'].sample(10000, random_state=42)])
        df = balanced_df

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(df['review'], df['rating'], test_size=0.1, random_state=42)

        # Text in numerical features
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        # Balance the dataset using SMOTE
        smote = SMOTE(random_state=42)
        X_train_vec, y_train = smote.fit_resample(X_train_vec, y_train)

        # Train model
        self.model = MultinomialNB()
        self.model.fit(X_train_vec, y_train)

        # Evaluate model
        y_pred = self.model.predict(X_test_vec)
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        # Save model and vectorizer
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)
        with open(self.vectorizer_path, 'wb') as f:
            pickle.dump(self.vectorizer, f)

    def load_model(self):
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(self.vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)

    def predict(self, review):
        review_vec = self.vectorizer.transform([review])
        prediction = self.model.predict(review_vec)
        return prediction[0]
