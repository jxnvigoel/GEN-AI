from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1=ChatGroq(model_name='llama-3.1-8b-instant')

parser=StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template='classify the sentiment of the feedback into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)
prompt2=PromptTemplate(
    template='write appropriate response to this positive feedback\n {feedback} ',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='write appropriate response to this negative feedback\n {feedback} ',
    input_variables=['feedback']
)

initial_chain=prompt1|model1|parser2

branch_chain=RunnableBranch(
    (lambda x: x.sentiment=='positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment=='negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: 'couldnot find sentiment')
)

final_chain=initial_chain|branch_chain
result=final_chain.invoke({'feedback':'this is a terrible product'})
print(result)
final_chain.get_graph().print_ascii()