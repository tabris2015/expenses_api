import uvicorn
from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="basic_api")
app.include_router(api_router, prefix="/v1")

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
