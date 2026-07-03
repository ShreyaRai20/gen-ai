from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional
import streamlit as st
import json

load_dotenv()

# -----------------------------
# Model
# -----------------------------
model = ChatMistralAI(model="mistral-small-2506")

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract movie info.\n{format_instructions}"),
    ("human", "{paragraph}")
])

# -----------------------------
# UI CONFIG
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Intelligence Extractor")
st.caption("Paste a movie description and get structured insights instantly.")

# Input
paragraph = st.text_area("Enter Movie Paragraph", height=200)

col1, col2 = st.columns([1, 1])

with col1:
    run = st.button("Extract", use_container_width=True)

with col2:
    clear = st.button("Clear", use_container_width=True)

if clear:
    st.rerun()

# -----------------------------
# Processing
# -----------------------------
if run:

    if not paragraph.strip():
        st.warning("Please enter a movie description.")
        st.stop()

    with st.spinner("Analyzing movie..."):

        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)

        try:
            movie = parser.parse(response.content)

            st.success("Extraction Complete!")

            # -----------------------------
            # BEAUTIFUL UI CARDS
            # -----------------------------

            st.subheader("Movie Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric("Title", movie.title or "N/A")
            col2.metric("Year", movie.release_year or "N/A")
            col3.metric("Rating", movie.rating or "N/A")

            st.divider()

            # Genres
            st.subheader("Genres")
            st.write(" | ".join(movie.genre) if movie.genre else "N/A")

            # Director
            st.subheader("Director")
            st.write(movie.director or "N/A")

            # Cast
            st.subheader("Cast")
            st.write(", ".join(movie.cast) if movie.cast else "N/A")

            # Summary card
            st.subheader("Summary")
            st.info(movie.summary)

            # JSON view (debug style)
            with st.expander("Raw JSON Output"):
                st.json(movie.model_dump())

        except Exception as e:
            st.error("Failed to parse response.")
            st.code(response.content)
            st.exception(e)