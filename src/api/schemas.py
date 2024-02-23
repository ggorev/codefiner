from pydantic import BaseModel, HttpUrl, Field


class InputScheme(BaseModel):
    link: HttpUrl = Field(examples=["https://gitlab.com/<file_path>"], description="Cсылка на GitLab файл.")


class OutputScheme(BaseModel):
    language: str = Field(examples=["python"])
    languages: dict = Field(examples=[{
        "python": 0.98,
        "java": 0.3,
        "javascript": 0.15
    }])
