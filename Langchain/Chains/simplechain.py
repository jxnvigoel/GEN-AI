from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt=PromptTemplate(
    template='generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model = ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain=prompt|model|parser

print(chain.invoke({'topic':'cars'}))