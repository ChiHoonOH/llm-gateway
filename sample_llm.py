from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 100
def llm(x):
    return x
@app.get("/generate/{prompt}")
#async def root():
def root(prompt:str): #차후 이걸로 대체 req:PromptRequest
    result = llm(prompt)
    return {"message": result}
