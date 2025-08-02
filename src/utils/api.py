import os
import getpass
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    return os.environ["OPENAI_API_KEY"]
