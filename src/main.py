from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/hello',
         summary='Hello word page',
         description='This api call get Hello word page',
         response_description='Return a Hello world message')
def index():
    return {'message': 'Hello world!'}


s
# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs have been provided.'}


@app.get('/blog/all', tags=['blog'])
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** is mandatory path parameter
    - **comment_id** is mandatory path parameter
    - **valid** is optional query parameter
    - **username** is optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Type of the blog is {type}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'The blog with id {id}'}
