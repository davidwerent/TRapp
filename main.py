from fastapi import FastAPI, APIRouter
from API import calendar_handler, auth, lk

app = FastAPI()

app.include_router(calendar_handler.router)
app.include_router(auth.router)

app.include_router(lk.router)

@app.get("/")
async def root():
    res = {
            'id': 0,
            'name': 'string',
            'isLogin': False
    }
    message = {
        'records': [
            res
        ]
    }
    return message



