from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World2"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")
