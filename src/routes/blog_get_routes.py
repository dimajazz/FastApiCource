from fastapi import APIRouter, Depends, status, Response
from enum import Enum
from typing import Optional

from routes.blog_post_routes import required_functionality

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


# @router.get('/all')
# def get_all_blogs():
#     return {'message': 'All blogs have been provided.'}


@router.get('/all')
def get_all_blogs(page=1, page_size: Optional[int] = None, req_param: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_param}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** is mandatory path parameter
    - **comment_id** is mandatory path parameter
    - **valid** is optional query parameter
    - **username** is optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Type of the blog is {type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'The blog with id {id}'}
