from fastapi import FastAPI
import datetime, time
app = FastAPI()

x = datetime.date(2024, 1, 13)
y = datetime.date.today()
z = datetime.date.today().year
odlic = str(x-y)

@app.get("/")
async def root():
    return f'zostałoooo: {odlic}'


@app.get("/items/{id}")
async def read(id):
    return {
        'data': {
            'name': id,
            'age': z - 2004,
            'odliczanie': ' '.join((str(x-y)).split()[:2])
        }
    }