from sqlalchemy import Column, Integer, String, Float

from src.data.database import Base


class Predictions(Base):
    __tablename__ = "predictions"

    request_id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    path_or_link = Column(String, nullable=False)
    file_extension = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    probability = Column(Float, nullable=False)
