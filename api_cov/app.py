import uvicorn
from fastapi import FastAPI
from .routes import items

app = FastAPI()
app.include_router(items.router)


@app.get("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)