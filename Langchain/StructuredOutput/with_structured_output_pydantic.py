from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel,Field
load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile")

# schema
class Review(BaseModel):
    key_benefits:list[str]=Field(description='key benefits of company')
    summary:str=Field(description='a brief summary of review')
    sentiment:Literal['pos','neg']=Field(description='return sentiment of review either negative or positive')
    pros:Optional[list[str]]=Field(default=None,description='pros of company')
    cons:Optional[list[str]]=Field(default=None,description='cons of company')
    recommend:Optional[bool]=Field(default=None,description='whether to recommend company or not')
structured_model=model.with_structured_output(Review)

result=structured_model.invoke('''Here's a sample long company review:

> I had a very positive experience working with this company. The organization provides a professional and supportive work environment where employees are encouraged to learn, grow, and take ownership of their responsibilities. The management team is approachable and values employee feedback, which creates a culture of trust and collaboration. The company invests in training programs and career development opportunities, helping individuals enhance their skills and advance in their careers.
>
> The workplace culture is inclusive and team-oriented, with colleagues who are knowledgeable and willing to help one another. Projects are often challenging and engaging, allowing employees to gain exposure to new technologies and industry best practices. The company also offers competitive compensation, good work-life balance, and employee-focused benefits. While there is always room for improvement in areas such as process optimization and communication across departments, the overall experience has been rewarding. I would recommend this company to professionals seeking a stable, growth-oriented, and positive workplace.
'''
)
print(result)