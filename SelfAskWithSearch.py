import os
from langchain.llms.openai import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from dotenv import load_dotenv

#load_dotenv()

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    openai_api_key = OPENAI_API_KEY,
    #model_name = "gpt-4",
    temperature = 0)
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

task = "Configuring Spam Filters to Reduce Unwanted Email"

tools = [
    Tool(
        name = "Intermediate Answer",
        func = search.run,
        description = "useful for a task that needs ask with search"

    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent = AgentType.SELF_ASK_WITH_SEARCH, verbose=True
)

self_ask_with_search.run(f"Explain a solution for this IT support task:{task}"
    
)