from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SInput(BaseModel):
    link: str = "https://gitlab.com/<project_path>"


class SOutput(BaseModel):
    language: str = "python"
    languages: dict = {"python": 0.98, "java": 0.30, "javascript": 0.15}


@app.post("/api/get_language")
def get_language(input: SInput) -> SOutput:
    ...
