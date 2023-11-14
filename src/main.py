from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from routes import blog_get_routes
from routes import blog_post_routes
from routes import user_routes
from routes import article_routes

from db import models
from db.database import engine

from utility.exceptions import StoryException


app = FastAPI()
app.include_router(user_routes.router)
app.include_router(blog_get_routes.router)
app.include_router(blog_post_routes.router)
app.include_router(article_routes.router)


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
