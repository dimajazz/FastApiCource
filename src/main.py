from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routes import (
    blog_get_routes,
    blog_post_routes,
    user_routes,
    article_routes,
    product_routes,
    auth_rotes,
    file_rotes
)
from templates import templates

from db import models
from db.database import engine

from utility.exceptions import StoryException


app = FastAPI()
app.include_router(user_routes.router)
app.include_router(blog_get_routes.router)
app.include_router(blog_post_routes.router)
app.include_router(article_routes.router)
app.include_router(product_routes.router)
app.include_router(auth_rotes.router)
app.include_router(file_rotes.router)
app.include_router(templates.router)


@app.get('/hello',
         summary='Hello word page',
         description='This api call get Hello word page',
         response_description='Return a Hello world message')
def index():
    return {'message': 'Hello world!'}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT, content={'detail': exc.name})


models.Base.metadata.create_all(engine)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/uploaded_files',
          StaticFiles(directory='uploaded_files'),
          name='uploaded_files')

app.mount('/templates/static',
          StaticFiles(directory='templates/static'),
          name='static')
