from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def root():
    return {"status": "Up and running."}