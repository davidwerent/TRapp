from fastapi import APIRouter, Body
from pydantic import BaseModel

from database.auth import check_auth_data, create_new_user


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
async def check(request: BaseAuthRequest):
    response = check_auth_data(request.data.phone, request.data.password)
    return response


@router.post('/auth/signup')
async def signup(request: BaseRegRequest):

    return create_new_user(request.data)
