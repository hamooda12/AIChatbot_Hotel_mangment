from fastapi import FastAPI

app = FastAPI(title="AI Hotel Management")

@app.get("/health")
def health():
    return {"status": "ok"}
