import uvicorn


from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    load_dotenv()
    print("Startup event triggered")

    