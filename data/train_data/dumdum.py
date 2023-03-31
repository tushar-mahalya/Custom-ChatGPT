from llama_index import GPTSimpleVectorIndex
from langchain import OpenAI
import configparser
import os

# loading config files for OpenAI API key and setting it as env. variable
config = configparser.ConfigParser()
config.read('secret_key.ini')
openai_key = config.get('OpenAI', 'secret_key')
os.environ["OPENAI_API_KEY"] = openai_key


def ask_me_anything(question):
    # Loading index files of textual data
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(question, response_mode='compact')

    print(color(f'>> {question}', 'blue', attrs=["bold"]))
    print(color('===================================================================================', 'yellow'),
          end='')
    print(f'{response.response}')
    print(color('===================================================================================', 'yellow'))

if __name__ == '__main__':
    ask_me_anything('Best model to work on financial data')