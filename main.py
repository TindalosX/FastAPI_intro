from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {"id": 1, "author": "luis", "title": "data structure", "content": "Data structures are methods for organizing, storing, and managing data..."},
    {"id": 2, "author": "noelle", "title": "algorithms", "content": "Algorithms are step-by-step procedures for solving problems, generally categorized into fundamental programming techniques..."},
    {"id": 3, "author": "nick", "title": "machin learnig", "content": "Machine Learning and AI Algorithms are used for data analysis and prediction..."},
]

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/api/posts")
def get_posts():
    return posts

#- Query parameters.
#Query parameters are function parameters that are not
#part of the path parameters, are automatically
#interpreted as "query" parameters.
@app.get("/api/posts/authors")
def get_author_post(name: str | None = None):
	if name:
		response = [post for post in posts if name == post['author'] ]
	else:
		response = {"message": "Not given name"}
	return response

#- Path parameter: {id}
#The value of the path parameter 'id' will be passed
#to the function as the argument 'id'.

#- Path parameters with types.
#In this case, the type of the path parameter 'id' is
#declared to be an int.
#With that type declaration, FastAPI gives you
#automatic request "parsing".
@app.get("/api/posts/{id}")
def get_post(id: int):
    return posts[id - 1]
