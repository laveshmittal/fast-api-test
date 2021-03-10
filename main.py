from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"success": True,"greetings_from":"Lavesh Mittal"}


