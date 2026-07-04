from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen-AgentWorld-35B-A3B",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal['pos', 'neg'] = Field(description="Return sentiment of the review either negative, positive, or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside the list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside the list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, its an absolute powerhouse The snapdragon processor makes everything lighthneing fast wheather i am gamimg, multitaskiking or editting photos. The 5000mah battery easilt lastes a full day even with heavy use, and the 45W fast chargeing is lifesaver.
                                 
The S-pen integration is a grefor note taking and quick scthough i dont ofetn use it whablew me away is the 200mp cnight mode is stunning,

the weight and size make uncomfortabble for one hand use samsung one ui still cobloatware 
. why?? do i need five difrentapps for the thing googleprovides. The 1300 dollars pricea hard pill to digest 
                                 
pros:
Insanely powerfull processor
stunning 200mp camera 
long battery
s pen
                                 
review by madhav lalit""")

print(result.name)