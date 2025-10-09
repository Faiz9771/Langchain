from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import os
import uvicorn

from dotenv import load_dotenv

# Load environment variables
load_dotenv()



os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

#interfacing fastapi
app = FastAPI(
    title="Jarvis",
    version="1.0",
    description="A simple api server"
)

#adding routes
add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0),
    path="/jarvis"
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
prompt = ChatPromptTemplate.from_template("Tell me something to discuss about {topic} with 100 words")

add_routes(
    app,
    prompt | model,
    path="/topic"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)