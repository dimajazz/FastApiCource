from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, Annotated

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    comments_num: int
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id': id, 'data': blog, 'version': version}


@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None,
        title='id of a comment',
        description='Some description for comment id',
        alias='commentId',
        deprecated=True),
    content: str = Body(
        ...,
        min_length=10,
        max_length=50,
        regex='^[a-z\s]*$')
):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content
    }
