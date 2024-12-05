from fastapi import FastAPI, HTTPException
from typing import Optional

# uvicorn main:app --reload
app = FastAPI()


@app.get("/")
async def home() -> dict[str, str]:
    return {"data": "message"}


@app.get("/contacts")
async def contacts() -> int:
    return 34


posts = [
    {"id": 1, "title": "News_1", "body": "Text_1"},
    {"id": 2, "title": "News_2", "body": "Text_2"},
    {"id": 3, "title": "News_3", "body": "Text_3"},
]


@app.get("/items")
async def items() -> list:
    return posts


@app.get("/items/{id}")
async def items_id(id: int = 1) -> dict:
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")  # вывод ошибки


@app.get("/search")
async def search(post_id: Optional[int] = None, post_title: Optional[str] = None) -> dict:
    # http://127.0.0.1:8000/search?post_id=1&post_title=News_1
    if post_id and post_title:
        for post in posts:
            if post["id"] == post_id and post["title"] == post_title:
                return post
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {"data": "No post_id provided"}
