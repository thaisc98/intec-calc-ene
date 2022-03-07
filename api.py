from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()


@app.get("/healthcheck")
async def root():
    return {"status": "Up and running."}


@app.get("/sumar")
def read_sumar(num1: int = 0, num2: int = 0):
    return  {
        "result": calc.sumar(num1, num2)
    }
