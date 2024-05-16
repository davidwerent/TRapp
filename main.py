from fastapi import FastAPI

from database.calendar import get_free_slot_func

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
    array = get_free_slot_func()
    events = {
        'events': array
    }
    return events

@app.post('/change_slot_busy/{event_id}')
async def change_slot_busy_router(event_id: int):
    return f'all is OK={event_id}'