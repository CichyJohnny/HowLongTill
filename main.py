from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import datetime, time
app = FastAPI()

x = datetime.date(2024, 1, 13)
y = datetime.date.today()
z = datetime.date.today().year
odlic = str(x-y)

@app.get("/")
async def start(req: bool=False, name: Optional[str] = ''):
    if req:
        return f'{name} zostałoooo: {odlic}'
    else:
        return None


@app.get("/items/{id}")
async def index(id: int):
    return {
        'data': {
            'name': id,
            'age': z - 2004,
            'odliczanie': ' '.join((str(x-y)).split()[:2])
        }
    }


class blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def blog(request: blog):
    ww = 'da' + 'ta'
    return {ww: f'blog is created as {request.title}'}
