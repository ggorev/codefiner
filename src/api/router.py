from fastapi import APIRouter

from src.api.schemas import InputScheme, OutputScheme
from src.service.db.db_api import DatabaseDTO
from src.service.gitlab.utils import get_text_from_repository, get_file_extension
from src.service.recognition.get_predict import get_predict

router = APIRouter(prefix="/api", tags=["Распознавание языка программирования"])


@router.post("/get_language", description="<b>Возвращает распознанный язык программирования</b>")
async def get_language(input: InputScheme) -> OutputScheme:
    link = str(input.link)
    file_extension = get_file_extension(link)
    prediction = get_predict(get_text_from_repository(link))
    await DatabaseDTO.add_prediction("link", link, file_extension, prediction)
    return prediction.prediction
