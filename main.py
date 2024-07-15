from fastapi import FastAPI, APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database_builder import *

templates = Jinja2Templates(directory="templates")

app = FastAPI(title="Haziq EXS Synergy", openapi_url="/openapi.json")

api_router = APIRouter()

database = database_builder()
column = ["ID", "Name", "Address", "Contacts", "Penalty"]


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/all")
def all(request: Request):
    return templates.TemplateResponse(
        "all.html", {"request": request, "database": database, "column": column}
    )


@app.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def register_post(
    name: str = Form(...),
    id: str = Form(...),
    address: str = Form(...),
    contact: str = Form(...),
):
    new_user = User(id, name, address, contact)
    database.append(new_user)
    return RedirectResponse(url="/register", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/update")
def update(request: Request):
    return templates.TemplateResponse("update.html", {"request": request})


@app.post("/update")
async def update_post(
    name: str = Form(...),
    id: str = Form(...),
    address: str = Form(...),
    contact: str = Form(...),
):
    for user in database:
        if int(user.id) == int(id):
            user.name = name
            user.contact = contact
            user.address = address
    return RedirectResponse(url="/update", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/borrow")
def borrow(request: Request):
    return templates.TemplateResponse("borrow.html", {"request": request})


@app.post("/borrow")
async def borrow_post(
    id: str = Form(...),
    title: str = Form(...),
    author: str = Form(...),
    book_id: str = Form(...),
):
    new_book = Book(title, author, book_id)
    for user in database:
        if int(user.id) == int(id):
            user.add_book(new_book)
    return RedirectResponse(url="/borrow", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/overdue")
def overdue(request: Request):
    return templates.TemplateResponse("overdue.html", {"request": request})
