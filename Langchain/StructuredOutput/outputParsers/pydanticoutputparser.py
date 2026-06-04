from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',
    task='text-generation',  
)
model=ChatHuggingFace(llm=llm)
class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int=Field(description='age of the person')
    city:str=Field(description='city of the person')
parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='generate name,age, city of a fictional {place} person /n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.invoke({'place':'german'})
# result=model.invoke(prompt)
# print(parser.parse(result.content))
chain=template|model|parser
print(chain.invoke({'place':'german'}))