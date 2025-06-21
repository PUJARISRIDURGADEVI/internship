from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

texts = ["I am feeling sad", "I need motivation", "Life is hard", "I’m so happy"]
labels = ["sad", "motivated", "sad", "happy","angry"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

joblib.dump((vectorizer, model), "mood_model.pkl")
