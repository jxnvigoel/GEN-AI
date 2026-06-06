from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt=PromptTemplate(
    template='generate a short 1 line joke on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='explain the {topic}',
    input_variables=['topic']
)

llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'monkey'}))