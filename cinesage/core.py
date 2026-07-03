from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

message = []

model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert information extraction assistant.

        Your task is to analyze the movie description provided by the user and extract the relevant information.

        Instructions:
        1. Read the entire movie paragraph carefully.
        2. Extract only the information explicitly stated in the text.
        3. If a field is missing or cannot be confidently determined, return null.
        4. Write the summary in 2 to 4 concise sentences capturing the main plot without adding information not present in the text.
        5. Return the output as valid JSON only.
        6. Do not include markdown, explanations, or extra text.

        Required JSON format:

        "title"
        "release_year"
        "genre"
        "director"
        "cast"
        "rating"
        "summary"

        Extraction Rules:
        - title: Official movie title.
        - release_year: Four-digit release year as an integer.
        - genre: List of genres.
        - director: List of directors.
        - cast: List of principal cast members.
        - rating: IMDb rating, Rotten Tomatoes score, MPAA rating, or other rating if explicitly mentioned. If multiple ratings are present, include the most prominent one as a string.
        - summary: A factual 2 to 4 sentence summary of the movie.
        """),
    (
        "human",
        """
        {MOVIE_PARAGRAPH}
        """
    )
])

user_input = input("please give movie parah: ")

final_prompt = prompt.invoke(input=dict(
    MOVIE_PARAGRAPH=user_input
))

response = model.invoke(final_prompt)

print(response.content)


