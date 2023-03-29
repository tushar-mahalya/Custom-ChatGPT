import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'hello tushar'}


@app.get('/welcome')
def get_name(name: str):
    return {'welcome to tushar sharma\'s instance': f'{name}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
