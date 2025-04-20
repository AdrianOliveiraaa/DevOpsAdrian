from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Alteração Teste - Branchs Paralelas"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "Branch Paralela"}