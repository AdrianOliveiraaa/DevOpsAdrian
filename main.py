from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "PUCPR - DEVOPS"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "Deu Certo"}