from typing import Literal

from pydantic import BaseModel, HttpUrl


class InputScheme(BaseModel):
    link: HttpUrl


class LanguagesScheme(BaseModel):
    python: float
    java: float
    javascript: float


class OutputScheme(BaseModel):
    language: Literal["python", "java", "javascript"]
    languages: LanguagesScheme
