import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

data = {
    "input": [
        "I feel low", "I'm sad", "depressed", "unhappy",
        "I'm excited", "I'm happy", "great day", "smiling",
        "I feel motivated", "let's work", "feeling strong"
    ],
    "mood": [
        "sad", "sad", "sad", "sad",
        "happy", "happy", "happy", "happy",
        "motivated", "motivated", "motivated"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["input"])
y = df["mood"]

model = MultinomialNB()
model.fit(X, y)

joblib.dump( (vectorizer,model), "mood_model.pkl")

