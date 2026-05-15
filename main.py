from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {"id": 1, "author": "Author 1", "title": "Post 1", "content": "Content 1"},
    {"id": 2, "author": "Author 2", "title": "Post 2", "content": "Content 2"},
    {"id": 3, "author": "Author 3", "title": "Post 3", "content": "Content 3"},
]

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/api/posts")
def get_posts():
    return posts
