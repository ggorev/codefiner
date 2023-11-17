from fastapi import APIRouter

from src.api.schemas import InputScheme, OutputScheme

router = APIRouter(prefix="/api", tags=["Распознавание языка программирования"])


@router.post("/get_language")
def get_language(input: InputScheme) -> OutputScheme:
    return {"language": "python", "languages": {"python": 0.98, "java": 0.30, "javascript": 0.15}}
