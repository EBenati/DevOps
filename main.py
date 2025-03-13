from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste1")
def teste():
    return {"teste1": "funcionando..."}

