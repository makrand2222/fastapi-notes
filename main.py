from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from enum import Enum

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient(
    "mongodb+srv://makrandmandhare:f2uO4TUzUXeQ8TGH@fastapi.hdfdzwv.mongodb.net/notes"
)


@app.get('/', response_class=HTMLResponse)
async def get_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append(
            {
                "id" : doc["_id"],
                "note": doc["note"]
            }
        )
    return templates.TemplateResponse("index.html",{"request": request, "newDocs" : newDocs})


@app.get('/items/{item_id}')
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
