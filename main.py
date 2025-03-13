import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste1")
def teste():
    return {"teste1": True, "num_aleatorio": random.randint(0, 20000)}

