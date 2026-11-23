import sqlite3

from fastapi import APIRouter, HTTPException, status

from app.database import add_article, get_all_articles, get_article_by_id
from app.schemas import ArticleCreate, ArticleResponse

# Create the articles router
router = APIRouter(prefix="/articles", tags=["Articles"])


# Get all Articles
@router.get("", response_model=list[ArticleResponse])
def list_articles(category: str | None = None):

    articles = get_all_articles(category)

    return articles


# Get One Article
@router.get("/{article_id}", response_model=ArticleResponse)
def read_article(article_id: int):

    article = get_article_by_id(article_id)

    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    return article


# Create article
@router.post("", response_model=ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(article: ArticleCreate):
    try:
        article_id = add_article(**article.model_dump())

    except sqlite3.IntegrityError as error:
        raise HTTPException(
            status_code=409, detail="An article with this URL already exists."
        ) from error

    saved_article = get_article_by_id(article_id)

    if saved_article is None:
        raise HTTPException(
            status_code=500, detail="Article was not found after insertion."
        )

    return saved_article
