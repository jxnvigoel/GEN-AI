from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile")

# schema
class Review(TypedDict):
    key_benefits:Annotated[list[str],'key benefits of company']
    summary:Annotated[str,'a brief summary of review']
    sentiment:Annotated[str,'return sentiment of review either negative or positive']
    pros:Annotated[Optional[list[str]],'pros of company']
    cons:Annotated[list[str],'cons of company']
    recommend:Annotated[Optional[bool],'whether to recommend company or not']
structured_model=model.with_structured_output(Review)

result=structured_model.invoke('''Here's a sample long company review:

> I had a very positive experience working with this company. The organization provides a professional and supportive work environment where employees are encouraged to learn, grow, and take ownership of their responsibilities. The management team is approachable and values employee feedback, which creates a culture of trust and collaboration. The company invests in training programs and career development opportunities, helping individuals enhance their skills and advance in their careers.
>
> The workplace culture is inclusive and team-oriented, with colleagues who are knowledgeable and willing to help one another. Projects are often challenging and engaging, allowing employees to gain exposure to new technologies and industry best practices. The company also offers competitive compensation, good work-life balance, and employee-focused benefits. While there is always room for improvement in areas such as process optimization and communication across departments, the overall experience has been rewarding. I would recommend this company to professionals seeking a stable, growth-oriented, and positive workplace.
'''
)
print(result)