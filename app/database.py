import sqlite3
from pathlib import Path

# Database location
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

DATABASE_PATH = DATA_DIR / "lol_esports.db"


# Database connection
def get_connection():
    # Create the data folder if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Connect to SQLite
    connection = sqlite3.connect(DATABASE_PATH)

    # Return rows that can be accessed by column name
    connection.row_factory = sqlite3.Row

    return connection


# Initialize database
def initialize_database():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS articles (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                title TEXT NOT NULL,

                url TEXT NOT NULL UNIQUE,

                publisher TEXT NOT NULL,

                author TEXT,

                published_at TEXT,

                content TEXT,

                category TEXT NOT NULL DEFAULT 'other',

                status TEXT NOT NULL DEFAULT 'pending_review',

                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP

            )
        """)

        connection.commit()

    finally:
        connection.close()


# Insert article
def add_article(title, url, publisher, author, published_at, content, category):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO articles (
                title,
                url,
                publisher,
                author,
                published_at,
                content,
                category
            )

            VALUES(?, ?, ?, ?, ?, ?, ?)
        
        """,
            (title, url, publisher, author, published_at, content, category),
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


# Retrieve articles
def get_all_articles():
    connection = get_connection()

    try:
        rows = connection.execute("""

            SELECT *
            FROM articles
            ORDER BY id

        """).fetchall()

        return [dict(row) for row in rows]

    finally:
        connection.close()


#  RUN DATABASE DEMONSTRATION

if __name__ == "__main__":
    initialize_database()

    print("Database initialized!")
    print("Location:", DATABASE_PATH)

    try:
        article_id = add_article(
            title="Sample: International tournament announcement",
            url="https://example.com/sample-tournament-announcement",
            publisher="Practice Publisher",
            author="Demo Author",
            published_at="2026-11-22T12:00:00+08:00",
            content="This is fictional sample content for database practice.",
            category="tournament",
        )

        print(f"\nSample article inserted. ID: {article_id}")

    except sqlite3.IntegrityError:
        print("\nDuplicate URL detected.")
        print("Sample article was not inserted again.")

    print("\nARTICLES IN DATABASE")
    print("--------------------")

    for article in get_all_articles():
        print("ID:", article["id"])
        print("Title:", article["title"])
        print("Publisher:", article["publisher"])
        print("Category:", article["category"])
        print("Status:", article["status"])
        print("--------------------")
