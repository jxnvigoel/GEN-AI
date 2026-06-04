from langchain_huggingface import HuggingFacePipeline

# HuggingFacePipeline runs models LOCALLY on your machine
# Using facebook/opt-125m — tiny open model, no login required, no gating

llm = HuggingFacePipeline.from_model_id(
    model_id='facebook/opt-125m',
    task='text-generation',
    pipeline_kwargs={
        'max_new_tokens': 100
    }
)

# For non-chat models, invoke directly on llm (not ChatHuggingFace)
result = llm.invoke("what is capital of India")
print(result)