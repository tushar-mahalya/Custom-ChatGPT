# importing important libraries
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')
openai_key = config.get('OpenAI', 'secret_key')

@st.cache_resource
def ChatBot():
    embeddings = OpenAIEmbeddings(openai_api_key = openai_key,
                                  allowed_special={"<|endoftext|>"})
    comments_embedding = FAISS.load_local("faiss_index", embeddings)
    retriever = comments_embedding.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key = openai_key),
                                     chain_type="stuff", retriever=retriever)
    return qa


st.set_page_config(page_title="Custom ChatGPT")

st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    }
</style>""", unsafe_allow_html=True)

# Sidebar contents
with st.sidebar:

    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/en/latest/index.html)
    - [Facebook AI Similarity Search (FAISS)](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/)
    - [GPT 3.5 Turbo Model](https://platform.openai.com/docs/models/gpt-3-5)

    ## Training Data
    The training data used for the chatbot was collected specifically from the top three subreddits related to data science on Reddit:
    - Machine Learning - [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
    - Artificial Intelligence - [r/artificial](https://www.reddit.com/r/Artificial/)
    - Data Science - [r/DataScience](https://www.reddit.com/r/DataScience/)
    
    The data collection process involved extracting the comments from the top 1000 posts within these subreddits. To accomplish this, a Python wrapper called PRAW (Python Reddit API Wrapper) was utilized in conjunction with the Reddit API. PRAW facilitated the seamless retrieval of comments from the most popular posts, ensuring that a comprehensive dataset was compiled for training the chatbot. By focusing on the most relevant and engaging discussions in the data science community, the chatbot's training was tailored to address the specific needs and inquiries of users in this domain.
    ''', unsafe_allow_html=True)
    st.write('Made with ❤️ by [Tushar Sharma](https://tushar-5harma.netlify.app/)')

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["How may I help you ?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
st.markdown("<h1 style='text-align: center;'>Custom ChatGPT</h1>", unsafe_allow_html=True)
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = ChatBot()
    response = chatbot.run(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))