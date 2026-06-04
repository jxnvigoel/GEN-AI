from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# load .env from parent Models/ folder
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',
    task='text-generation',
    provider='novita',   # free provider available on HF free tier
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("what is capital of India")
print(result.content)