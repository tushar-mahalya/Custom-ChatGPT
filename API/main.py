import uvicorn
from fastapi import FastAPI
import configparser
from pydantic import BaseModel
from llama_index import GPTSimpleVectorIndex
import os

# Creating local runtime instance of FastAPI
app = FastAPI()


class Ask_Question(BaseModel):
    question: str


# loading config files for OpenAI API key and setting it as env. variable
config = configparser.ConfigParser()
config.read('secret_key.ini')
openai_key = config.get('OpenAI', 'secret_key')
os.environ["OPENAI_API_KEY"] = openai_key



@app.get('/')
async def index():
    return {'message': 'Hello Tushar'}


@app.post('/response')
async def response(question: Ask_Question):
    index = GPTSimpleVectorIndex.load_from_disk('/home/tushar_sharma/PycharmProjects/Custom-ChatGPT/data/train_data/index.json')
    bot_response = index.query(question, response_mode='compact')
    return {'answer': f'{bot_response}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
