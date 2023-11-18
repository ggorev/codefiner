from typing import Literal

from pydantic import BaseModel, HttpUrl, Field


class InputScheme(BaseModel):
    link: HttpUrl = Field(examples=["https://gitlab.com/<project_path>"], description="Cсылка на GitLab проект")


class LanguagesScheme(BaseModel):
    python: float = Field(examples=[0.98])
    java: float = Field(examples=[0.30])
    javascript: float = Field(examples=[0.15])


class OutputScheme(BaseModel):
    language: Literal["python", "java", "javascript"] = Field(examples=["python"])
    languages: LanguagesScheme
