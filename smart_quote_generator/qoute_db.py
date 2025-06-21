import sqlite3

# Connect to database (creates if it doesn't exist)
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# Create quotes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT NOT NULL,
        author TEXT,
        mood TEXT NOT NULL
    )
''')

# Sample quotes to insert
sample_quotes = [
    ("Believe you can and you're halfway there.", "Theodore Roosevelt", "motivated"),
    ("Tough times never last, but tough people do.", "Robert Schuller", "motivated"),
    ("It's okay to cry. It’s okay to feel down.", "Unknown", "sad"),
    ("Sadness flies away on the wings of time.", "Jean de La Fontaine", "sad"),
    ("Happiness is not something ready-made. It comes from your own actions.", "Dalai Lama", "happy"),
    ("For every minute you are angry you lose sixty seconds of happiness.", "Ralph Waldo Emerson", "happy"),
    ("Speak when you are angry and you will make the best speech you will ever regret.","Ambrose Bierce","angry"),
    ("Do not let your fears choose your destiny.","Unknown","fear"),
    ("You are never too old to set another goal.","C.S. Lewis","hopeful"),
    ("Anger is an acid that can do more harm to the vessel.","Mark Twain","angry"),
    ("The best way out is always through.","Robert Frost","depressed"),
    ("Push yourself, because no one else is going to do it for you.","Unknown","motivated"),
    ("Keep your face always toward the sunshine—and shadows will fall behind you.","Walt Whitman","optimistic"),
    ("When everything seems to be going against you, remember that the airplane takes off against the wind.","Henry Ford","frustrated"),
    ("Life is what happens when you're busy making other plans.","John Lennon","reflective"),
    ("Happiness is not by chance, but by choice.","Jim Rohn","joyful"),
    ("Courage is resistance to fear, mastery of fear—not absence of fear.","Mark Twain","brave"),
    ("The mind is everything. What you think you become.","Buddha","focused"),
    ("What lies behind us and what lies before us are tiny matters compared to what lies within us.","Ralph Waldo Emerson","strong"),
    ("Every strike brings me closer to the next home run.","Babe Ruth","hopeful"),
    ("It always seems impossible until it’s done.","Nelson Mandela","determined"),
    ("Light tomorrow with today.","Elizabeth Barrett Browning","inspired"),
    ("A smooth sea never made a skilled sailor.","Franklin D. Roosevelt","resilient"),
    ("Keep going. Everything you need will come to you at the perfect time.","Unknown","patient")
]

# Insert quotes
cursor.executemany("INSERT INTO quotes (quote, author, mood) VALUES (?, ?, ?)", sample_quotes)

conn.commit()
conn.close()

print("quotes.db created and populated successfully.")
