from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',
    task='text-generation',  
)
model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact_1',description='fact 1 about topic'),
    ResponseSchema(name='fact_2',description='fact 2 about topic'),
    ResponseSchema(name='fact_3',description='fact 3 about topic')
]
parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template="give 3 facts about the {topic}/n{format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}

)
prompt=template.format(topic='ai')
result=model.invoke(prompt)
print(parser.parse(result.content))