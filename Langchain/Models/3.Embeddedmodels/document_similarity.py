from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2' )
documents=[
    "Virat Kohli is one of India's greatest batsmen and a former captain known for his consistency.",
    "Rohit Sharma is the captain of India and famous for his elegant batting and double centuries in ODIs.",
    "MS Dhoni is a legendary wicketkeeper-batsman who led India to multiple ICC trophies.",
    "Sachin Tendulkar is known as the 'God of Cricket' and holds numerous batting records.",
    "Jasprit Bumrah is India's premier fast bowler, renowned for his unique action and deadly yorkers."
]
query='tell me about virat kohli'

doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

similarities=cosine_similarity([query_embedding],doc_embedding)[0]
index,score=sorted(list(enumerate(similarities)),key=lambda x:x[1],reverse=True)[0]
print(f"Most similar document is at index {index} with score {score}")
print(documents[index])
