from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
)
chat_model = ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='suggest a 5 line description on {topic}',
    input_variables=['topic']
)
chain=LLMChain(llm=chat_model,prompt=prompt)
print(chain.run('AI'))