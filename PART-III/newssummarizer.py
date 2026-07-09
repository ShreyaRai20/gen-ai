from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

tavily_search_tool = TavilySearchResults(max_results=5)

llm_model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_template(
    """
        you are a helpful news Assistant
        summarize {news}
    """
)

chain = prompt | llm_model | StrOutputParser()

tavily_news = tavily_search_tool.run("search top 5 2026 news")

response = chain.invoke({
    "news": tavily_news
})

print(response)

print("name " + tavily_search_tool.name)
print(tavily_search_tool.description)
print(tavily_search_tool.args)