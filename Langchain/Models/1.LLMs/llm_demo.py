from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# load api key from parent directory's .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

llm = ChatGroq(model='llama-3.3-70b-versatile')
result = llm.invoke("what is capital of India")
print(result.content)