# here we're making a application that prints joke and count how many letters are in joke .
# sequential chain(prompt,model,parser) + lambda + passthrough

""" RUNNABLE LAMBDA-
it is used to convert any function into a runnable.
"""
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough
load_dotenv()

prompt=PromptTemplate(
    template='generate a short 1 line joke on {topic}',
    input_variables=['topic']
)

llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)

def word_count(text):
    return len(text.split())
parallel=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(chain,parallel)
print(final_chain.invoke({'topic':'monkey'}))
