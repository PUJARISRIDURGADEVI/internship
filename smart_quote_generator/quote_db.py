import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        mood TEXT NOT NULL
    )
""")

# Insert sample quotes
sample_quotes = [
    ("Keep pushing forward!", "motivated"),
    ("It's okay to rest, take your time.", "sad"),
    ("Smile, life is beautiful.", "happy"),
    ("Every day is a second chance.", "sad"),
    ("You are unstoppable!", "motivated")
]

cursor.executemany("INSERT INTO quotes (text, mood) VALUES (?, ?)", sample_quotes)

# Commit and close
conn.commit()
conn.close()

print("quotes.db created successfully!")


