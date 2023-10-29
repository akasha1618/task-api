import os
from langchain.llms.openai import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    openai_api_key = OPENAI_API_KEY,
    #model_name = "gpt-4",
    temperature = 0)
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

task = "hey its harry and i really dont know how to hande a hardware issue again this time its laptop screen flickering intermittently any suggestions on what to do next anyone free to help"

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

self_ask_with_search.run(f"find a solution for the customer problem in this message: {task}"
    
)
