# from mylib.logic import wiki

# result = wiki()
# result = result
# print(wiki())
from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str, num2: int):
    """Page to search wikipedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""
    print(f"Passed in name: {name}")
    result = wikiphrases(name)
    print(f"Result: {result}")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8081, host="0.0.0.0")
