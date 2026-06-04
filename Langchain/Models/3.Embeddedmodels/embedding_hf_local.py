from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# text='Delhi is capital of india'
doc=[
    'hello',
    'what is the temprature now',
    'how are you'
]
vector=embedding.embed_documents(doc)
print(str(vector[:3]))
# 384 dimensional vectors by default