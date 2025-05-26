from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from bson import ObjectId

note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get('/', response_class=HTMLResponse)
async def get_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append(
            {
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"],
                "important": doc["important"] 
                }
            )
    print("newDocs: ",newDocs)
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )


@note.get('/items/{item_id}')
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@note.post('/')
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return RedirectResponse("/api/", status_code=302)

@note.post('/delete/{note_id}')
async def delete_note(note_id: str):
    conn.notes.notes.delete_one({"_id":ObjectId(note_id)})
    return RedirectResponse("/api/", status_code=302)