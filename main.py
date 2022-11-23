from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg":"Aprendendo a fazer o processo de Deploy."}
