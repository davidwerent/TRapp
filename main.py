from fastapi import FastAPI

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


@app.get('/without_key')
async def check():
    res = {
        'id': 0,
        'name': 'string',
        'isLogin': False
    }
    array = [res]
    return array