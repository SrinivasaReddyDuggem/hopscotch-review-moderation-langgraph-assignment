import os, re, json, time, operator
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="openai/gpt-4o-mini", temperature=0,
                 base_url="https://openrouter.ai/api/v1",
                 api_key=os.getenv("OPENROUTER_API_KEY"))
print("Model ready:", llm.model_name)