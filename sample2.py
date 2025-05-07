from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
#async def root():
def root(name:str):
    return {"message": "not home_"+name}


@app.get("/home")
def home(name:str):
    return {"message": "home"}
