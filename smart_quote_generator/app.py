from flask import Flask, render_template, request
import sqlite3
import joblib

app = Flask(__name__, template_folder='templates')  # <=== specify templates folder


# Load ML model and vectorizer
vectorizer, model = joblib.load("mood_model.pkl")

def get_quotes_by_mood(mood):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT quote, author FROM quotes WHERE mood = ?", (mood,))
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    mood = ""
    quotes = []
    if request.method == "POST":
        user_input = request.form["text"]

    # Instead of prediction, just use direct mood input
        mood = user_input.lower().strip()
        quotes = get_quotes_by_mood(mood)

    return render_template("index.html", mood=mood, quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)
