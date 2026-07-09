from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
model = ChatMistralAI(model="mistral-small-2506")

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        extract movie information from the paragraph
        {format_instructions}
        """),
    (
        "human",
        """
        {paragraph}
        """
    )
])

para = input("please give your parah: ")

final_prompt = prompt.invoke(input=dict(
    paragraph=para,
    format_instructions=parser.get_format_instructions()
))

response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)

print(movie_data)


