from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    comments_num: int
    published: Optional[bool]
    tags: list[str] = []
    metadata: dict[str, str] = {}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id': id, 'data': blog, 'version': version}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: str = Query(
        None,
        title='Title of a comment',
        description='Some description for comment title',
        alias='commentTitle',
        deprecated=True),
    content: str = Body(
        ...,
        min_length=10,
        max_length=50,
        pattern=r'^[a-z\s]*$'),
    version: list[float] = Query(..., alias='v'),
    comment_id: int = Path(gt=1, le=15),
):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'comment_title': comment_title,
        'content': content,
        'version': version,
    }


def required_functionality():
    return {'message': 'A message that implemented by Dependencies'}
