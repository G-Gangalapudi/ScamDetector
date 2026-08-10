from fastapi import FastAPI

app = FastAPI(title="Scam Intelligence")

@app.get("/")
def read_root():
    return {"message": "Scam Intelligence API"}
