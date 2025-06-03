from fastapi import APIRouter, Body, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse

templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get("/lk", response_class=HTMLResponse)
async def lk(request: Request):
    return templates.TemplateResponse("lk.html", {"request": request})


@router.get("/lk/get_info", response_class=HTMLResponse)
async def get_info(request: Request):
    return templates.TemplateResponse("get_info.html", {"request": request})


