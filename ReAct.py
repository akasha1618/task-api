import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults
from langchain.utilities.tavily_search import TavilySearchAPIWrapper


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
search = TavilySearchAPIWrapper(tavily_api_key=TAVILY_API_KEY)
tavily_tool = TavilySearchResults(api_wrapper=search)


agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

task2 = "Configuring Spam Fitlers to Reduce Unwanted Email?"


solution2 = agent_chain.run(f"Explain a solution for this IT support task: {task2}")
print(solution2)


