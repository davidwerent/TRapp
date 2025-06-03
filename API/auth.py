from fastapi import APIRouter, Body, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from database.auth import check_auth_data, create_new_user

templates = Jinja2Templates(directory='templates')

class AuthRequest(BaseModel):
    phone: str = None
    password: str = None
    device_id: str = None


class BaseAuthRequest(BaseModel):
    method: str
    token: str
    data: AuthRequest()


class RegInfo(BaseModel):
    user_id: int = None


class RegResponse(BaseModel):
    status: int
    message: str
    data: RegInfo()


class RegRequest(BaseModel):
    phone: str = None
    password: str = None
    firstname: str = None
    lastname: str = None
    device_id: str = None
    flat: int = None


class BaseRegRequest(BaseModel):
    method: str
    token: str = None
    data: RegRequest()


router = APIRouter()


@router.post('/auth/signin')
async def check(request: Request,
                phone_number: str = Form(...),
                password: str = Form(...)):
    print(phone_number)
    print(password)

    response = check_auth_data(phone_number, password)
    if response.get('status') == 200:
        target_url = '/lk'
        return RedirectResponse(target_url, status_code=303)
    else:
        return response

@router.get('/auth/signin')
async def show_signin(request: Request):
    print(request)
    return templates.TemplateResponse('login.html', {'request': request})


@router.post('/auth/signup')
async def signup(request: Request,
                 first_name: str = Form(...),
                 phone_number: str = Form(...),
                 password: str = Form(...)):

    result = create_new_user(first_name, phone_number, password)
    if result.get('status') == 2001:
        return RedirectResponse('/lk', status_code=303)
    else:
        return result
