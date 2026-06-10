from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv

load_dotenv()

text='''Artificial intelligence is transforming healthcare by enabling early disease detection and personalized treatment plans. At the same time, climate change is increasing health risks, such as heat-related illnesses and the spread of infectious diseases. By analyzing environmental and medical data together, AI can help predict outbreaks and improve public health responses. Integrating technology with climate awareness creates smarter healthcare systems that are better prepared to handle future global challenges.
'''
splitter=SemanticChunker(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

result=splitter.split_text(text)

# print(result)   
print(len(result))