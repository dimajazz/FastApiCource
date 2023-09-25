from fastapi import FastAPI
from routes import blog_get_routes
from routes import blog_post_routes

app = FastAPI()
app.include_router(blog_get_routes.router)
app.include_router(blog_post_routes.router)


@app.get('/hello',
         summary='Hello word page',
         description='This api call get Hello word page',
         response_description='Return a Hello world message')
def index():
    return {'message': 'Hello world!'}