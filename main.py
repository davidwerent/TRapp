from fastapi import FastAPI

from database.calendar import get_calendar

app = FastAPI()


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


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/get_free_slot')
async def check():
    array = get_calendar(show_free_slot=True)
    events = {
        'events': array
    }
    return events