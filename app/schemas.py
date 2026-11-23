from pydantic import BaseModel, Field


# Information required when creating an article
class ArticleCreate(BaseModel):
    title: str = Field(min_length=1)

    url: str = Field(min_length=1)

    publisher: str = Field(min_length=1)

    author: str | None = None

    published_at: str | None = None

    content: str | None = None

    category: str = "other"


# Information returned by the API
class ArticleResponse(BaseModel):
    id: int

    title: str

    url: str

    publisher: str

    author: str | None

    published_at: str | None

    content: str | None

    category: str

    status: str

    created_at: str
