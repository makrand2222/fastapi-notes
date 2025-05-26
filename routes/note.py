from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn


note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get('/', response_class=HTMLResponse)
async def get_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({"id": doc["_id"], "note": doc["note"]})
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )


@note.get('/items/{item_id}')
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
