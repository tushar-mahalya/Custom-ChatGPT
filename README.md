# <p align = "center">__Custom ChatGPT__</p>
[![Repo Size](https://img.shields.io/github/repo-size/tushar-mahalya/Custom-ChatGPT?style=flat-square)](https://github.com/tushar-mahalya/Custom-ChatGPT)  ![License](https://img.shields.io/badge/license-MIT-red.svg)  ![Project Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)


By combining the wealth of knowledge shared within the Reddit data science community, the power of OpenAI's GPT-3.5-Turbo model, the efficiency of the [Langchain](https://python.langchain.com/) framework, and the retrieval capabilities of the [FAISS](https://ai.facebook.com/tools/faiss/#:~:text=FAISS%20contains%20algorithms%20that%20search,and%20GPU%20support%20via%20CUDA.) library, we create a bespoke ChatGPT that possesses the collective wisdom and expertise of the Reddit community. Our custom ChatGPT is poised to engage in intelligent, informative, and contextually relevant conversations on topics spanning data science, machine learning, artificial intelligence, and more. This project serves as a testament to the extraordinary potential of combining state-of-the-art language models with community-generated knowledge to push the boundaries of conversational AI.
#### Demo Video -
<img src = "resources/CustomGPT_demo.gif" />

## Getting started with the ChatBot

The ChatBot is not currently deployed due to the cost associated with accessing the GPT model through my personal OpenAI API key. However, you can still run the ChatBot on your local machine by following the instructions below. Make sure you have enough credits available for using the ChatBot.

To run the ChatBot locally, please follow these detailed steps:

1. Clone the repository to your local machine by executing the following command in your terminal:
   
       git clone https://github.com/tushar-mahalya/Custom-ChatGPT.git
       cd Custom-ChatGPT
   
2. Create and activate a virtual environment (optional but recommended):

       python3 -m venv venv
       source venv/bin/activate
  
4. Install the necessary dependencies by running the following command in your terminal:
   
       pip install -r requirements.txt
   
5. Configure your personal OpenAI API secret key by running the following command in your terminal:

       echo -e '[OpenAI]\nsecret_key = YOUR_PERSONAL_API_SECRET_KEY' > credentials.ini
   Replace YOUR_PERSONAL_API_SECRET_KEY with your actual OpenAI API secret key. This step ensures that the ChatBot can access the OpenAI GPT model using your credentials.
   
6. Start the application by running the following command in your terminal:

       streamlit run app.py
   This command will launch the ChatBot application and provide you with a local web address.
   
7. Open your web browser and enter the following URL in the address bar:
   
       http://localhost:8501/
   This will open the ChatBot interface in your web browser, allowing you to interact with the ChatBot locally.

Please note that running the ChatBot locally requires a suitable environment with Python and the necessary dependencies. Ensure that you meet the requirements and follow the instructions carefully to set up and run the ChatBot on your machine. Enjoy your conversation with the ChatBot!

## Introduction


## <u>Hardware Specification</u>
For this project I've used [Amazon Sagemaker Studio Lab](https://studiolab.sagemaker.aws/) EC2-Instance which have the following specs - 
| Component | Specification |
| --- | --- |
| CPU | Intel® Xeon® Platinum 8259CL |
| Architecture | x86_64 |
| RAM | 16GB |
| Storage | 15GB (AWS S3 Bucket) |
| GPU | NVIDIA® Tesla T4 |
| CUDA Version | 11.4 |
| V-RAM | 15GB |

## Contributing

If you would like to contribute to the project, you can follow the steps below:

1. Fork the repository to your GitHub account.
2. Clone the repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes to the codebase.
5. Push your changes to your forked repository.
6. Create a pull request from your forked repository to the original repository.

## License

This project is licensed under the MIT License. You are free to use, modify and distribute the code as per the license terms
