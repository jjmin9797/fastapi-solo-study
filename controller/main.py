from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    response: int
    name: str
    content: str


app = FastAPI()


@app.get("/")
def main():
    return {"ResponseStatus": "200", "name": "Success", "content": "Good!!"}
