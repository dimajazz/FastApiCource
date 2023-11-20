from pydantic import BaseModel


# Article model has a connection with UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: list[Article] = []

    class Config():
        from_attributes = True


# User model has a connection with ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config():
        from_attributes = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        from_attributes = True


class ProductBase(BaseModel):
    title: str
    description: str
    price: float
