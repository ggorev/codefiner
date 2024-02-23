import asyncio

import typer
import uvicorn
from fastapi import FastAPI
from pydantic import FilePath
from src.api.router import router
from src.service.db.db_api import DatabaseDTO
from src.service.gitlab.utils import get_file_extension
from src.service.recognition.get_predict import get_predict

app = FastAPI()
app.include_router(router)
typer = typer.Typer()


@typer.command()
def start_api():
    config = uvicorn.Config("src.main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()


@typer.command()
def get_language_for_local(filepath: FilePath):
    with open(filepath, 'r', encoding='utf-8') as file:
        file_text = file.read()
    file_extension = get_file_extension(str(filepath))
    prediction = get_predict(file_text)
    asyncio.run(DatabaseDTO.add_prediction("filepath", str(filepath), file_extension, prediction))
    print(prediction.prediction['language'].title())


if __name__ == "__main__":
    typer()
