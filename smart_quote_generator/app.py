from flask import Flask, render_template, request
import joblib
import json

# Load model and vectorizer
vectorizer, model = joblib.load("mood_model.pkl")

# Load quotes
with open("quote.json", "r") as f:
    quotes = json.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    quote = ""
    mood = ""
    if request.method == "POST":
        user_input = request.form["mood"]
        X = vectorizer.transform([user_input])
        mood = model.predict(X)[0]

        # Find first matching quote
        for q in quotes:
            if q["mood"] == mood:
                quote = q["text"]
                break

    return render_template("index.html", quote=quote, mood=mood)

if __name__ == "__main__":
    app.run(debug=True)
