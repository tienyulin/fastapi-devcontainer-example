from fastapi import FastAPI

app = FastAPI(title="FastAPI DevContainer Example")


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI DevContainer!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
