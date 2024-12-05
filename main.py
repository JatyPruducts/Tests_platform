from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

# uvicorn main:app --reload
app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User


users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 25},
    {"id": 3, "name": "Bob", "age": 40},
]

posts = [
    {"id": 1, "title": "News_1", "body": "Text_1", "author": users[1]},
    {"id": 2, "title": "News_2", "body": "Text_2", "author": users[0]},
    {"id": 3, "title": "News_3", "body": "Text_3", "author": users[2]},
]


@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get("/items/{id}")
async def items_id(id: int) -> Post:
    for post in posts:
        if post["id"] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Item not found")  # вывод ошибки


@app.get("/search")
async def search(post_id: Optional[int] = None, post_title: Optional[str] = None) -> Dict[str, Optional[Post]]:
    # http://127.0.0.1:8000/search?post_id=1&post_title=News_1
    if post_id and post_title:
        for post in posts:
            if post["id"] == post_id and post["title"] == post_title:
                return {"data": Post(**post)}
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {"data": None}
