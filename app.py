import os
import faiss
import numpy as np
import logging
import pandas as pd
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.utilities import SerpAPIWrapper
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults
from langchain.utilities.tavily_search import TavilySearchAPIWrapper

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


data = pd.read_csv('it_support_all.csv')


class TaskDescription(BaseModel):
    task_description: str

app = FastAPI()
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
index = faiss.read_index('faiss_index2.index')

#endpoint for similarity search with faiss
@app.post('/search/')
async def search_similar_tasks(task_description: TaskDescription):
    ##print(f"Received task description: {task_description.task_description}")
    # Generate embedding for the input task description
    query_embedding = model.encode([task_description.task_description])[0]
    # Search the Faiss index for similar task embeddings
    D, I = index.search(np.array([query_embedding]), k=10)  # Search the top 10 similar tasks
    similar_tasks = data.iloc[I[0]]['Description'].tolist()
    return {"result": similar_tasks}

#LangChain Agent with SelfAskWithSearch and SerpAPI web search
llm = OpenAI(
    openai_api_key = OPENAI_API_KEY,
    temperature = 0
    #model_name = "gpt-4"
)
searchOnlineSerpAPI = SerpAPIWrapper(serpapi_api_key =SERPAPI_API_KEY)
tools = [
    Tool(
        name = "Intermediate Answer",
        func = searchOnlineSerpAPI.run,
        description="Useful for a task that needs online search"

    )
]

agent_executor = initialize_agent(tools, llm, agent = AgentType.SELF_ASK_WITH_SEARCH,verbose=False)

class TaskInput(BaseModel):
    task: str

#endpoint for SelfAskWithSearch agent solution 
@app.post('/serpapi')
async def get_task_solution(task_input: TaskInput):
    task = task_input.task
    solution = agent_executor.invoke({"input": f"Explain a solution for this IT support task: {task}"})
    return {"result": solution["output"]}

#LangChain Agent with Structured ReAct and Tavily.ai web search
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
search = TavilySearchAPIWrapper(tavily_api_key=TAVILY_API_KEY)
tavily_tool = TavilySearchResults(api_wrapper=search)

agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

class TaskInput2(BaseModel):
    task2: str

#endpoint for Structed ReAct agent solution 
@app.post('/tavily')
async def get_task_solution2(task_input2: TaskInput2):
    task2 = task_input2.task2
    solution2 = agent_chain.run(f"Explain a solution for this IT support task: {task2}")
    return {"result": solution2}









    

