from typing import Literal

from sqlalchemy import insert
from src.api.models import Predictions
from src.data.database import async_session_maker
from src.service.recognition.get_predict import Prediction


class DatabaseDTO:
    @classmethod
    async def add_prediction(cls, type: Literal["link", "filepath"], path_or_link, file_extension,
                             prediction: Prediction):
        """
        INSERT INTO predictions (type, path_or_link, file_extension, prediction, probability)
        VALUES ('link', 'https://gitlab.com/<project_path>', '.py', 'python', '0.98')
        """

        async with async_session_maker() as session:
            query = (insert(Predictions).values(type=type, path_or_link=path_or_link, file_extension=file_extension,
                                                prediction=prediction.prediction['language'],
                                                probability=prediction.probability).returning(Predictions))
            new_prediction = await session.execute(query)
            await session.commit()
            return new_prediction.scalar()
