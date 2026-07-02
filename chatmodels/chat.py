from dotenv import load_dotenv

load_dotenv()

# import os
# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model="gpt-5.5")

# response = model.invoke("what is machine learning?")

# print(response.content)

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

from langchain_huggingface import HuggingFaceEmbeddings



from langchain.chat_models import init_chat_model

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
model2 = ChatGroq(model="llama-3.1-8b-instant")

response = model.invoke("what is machine learning?")
response2 = model2.invoke("what is machine learning?")

print("response1: " + response.content)
print("response2: " + response2.content)