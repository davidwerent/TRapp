from fastapi import APIRouter, Body
from pydantic import BaseModel

from database.auth import check_auth_data


class AuthRequest(BaseModel):
    phone: str = None
    password: str = None
    device_id: str = None


class BaseAuthRequest(BaseModel):
    method: str
    token: str
    data: AuthRequest()


router = APIRouter()


@router.post('/auth/login')
async def check(request: BaseAuthRequest):
    response = check_auth_data(request.data.phone, request.data.password)
    return response


