from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# load .env from parent Models/ folder
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0,max_tokens=10)
# temprature is used to control the randomness of the response generated
result = model.invoke("write a line on india")
# print(result)          
print(result.content)     