import typer
import uvicorn
from fastapi import FastAPI
from pydantic import FilePath

from src.api.router import router

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
    ...


if __name__ == "__main__":
    typer()
