from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

def load_llm():
    return ChatOpenAI(model="gpt-4o", temperature=0)

def create_agent(llm, csv_file):
    return create_csv_agent(llm, csv_file, verbose=True, allow_dangerous_code=True)
