# Adapted based on LlamaIndex documentation https://gpt-index.readthedocs.io/en/latest/index.html
# and Dan Shipper's work https://www.lennysnewsletter.com/p/i-built-a-lenny-chatbot-using-gpt

from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define LLM (ChatGPT gpt-3.5-turbo)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0,
                                                model_name="gpt-3.5-turbo",
                                                max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size,
                                 num_outputs,
                                 max_chunk_overlap,
                                 chunk_size_limit = chunk_size_limit)
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents,
        llm_predictor = llm_predictor,
        prompt_helper = prompt_helper,
        disallowed_special = ()
    )

    index.save_to_disk('index.json')
    print('\033[32m' + 'Text Embeddings created Succesfully ! \nStored in \'train_data/index.json\'' + '\033[0m')

    return index