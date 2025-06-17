from flask import Flask, render_template, request
import joblib
import sqlite3

# Load model and vectorizer
vectorizer, model = joblib.load("mood_model.pkl")

app = Flask(__name__)

def get_quote_by_mood(mood):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM quotes WHERE mood = ? LIMIT 1", (mood,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No quote found for this mood."

@app.route("/", methods=["GET", "POST"])
def index():
    quote = ""
    mood = ""
    if request.method == "POST":
        user_input = request.form["mood"]
        X = vectorizer.transform([user_input])
        mood = model.predict(X)[0]

        # Fetch quote from database
        quote = get_quote_by_mood(mood)

    return render_template("index.html", quote=quote, mood=mood)

if __name__ == "__main__":
    app.run(debug=True)
