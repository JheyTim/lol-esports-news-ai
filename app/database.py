import sqlite3
from pathlib import Path

# =====================================
# 1. DATABASE LOCATION
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

DATABASE_PATH = DATA_DIR / "lol_esports.db"


# =====================================
# 2. DATABASE CONNECTION
# =====================================


def get_connection():

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


# =====================================
# 3. INITIALIZE DATABASE
# =====================================


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


# =====================================
# 4. INSERT ARTICLE
# =====================================


def add_article(
    title,
    url,
    publisher,
    author=None,
    published_at=None,
    content=None,
    category="other",
):

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

            VALUES (?, ?, ?, ?, ?, ?, ?)

        """,
            (title, url, publisher, author, published_at, content, category),
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


# =====================================
# 5. GET ALL ARTICLES
# =====================================


def get_all_articles(category=None):

    connection = get_connection()

    try:
        if category is None:
            rows = connection.execute("""

                SELECT *
                FROM articles
                ORDER BY id

            """).fetchall()

        else:
            rows = connection.execute(
                """

                SELECT *
                FROM articles
                WHERE LOWER(category) = LOWER(?)
                ORDER BY id

            """,
                (category,),
            ).fetchall()

        return [dict(row) for row in rows]

    finally:
        connection.close()


# =====================================
# 6. GET ONE ARTICLE
# =====================================


def get_article_by_id(article_id):

    connection = get_connection()

    try:
        row = connection.execute(
            """

            SELECT *
            FROM articles
            WHERE id = ?

        """,
            (article_id,),
        ).fetchone()

        return dict(row) if row is not None else None

    finally:
        connection.close()
