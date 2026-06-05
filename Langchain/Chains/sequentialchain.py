from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

promp1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a 50 words summary of the {report}',
    input_variables=['report']
)

llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain=promp1|model|parser|prompt2|model|parser

print(chain.invoke({'topic':'toyota cars'}))
chain.get_graph().print_ascii()