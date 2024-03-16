from typing import Optional, Any
from models.Category import Category
from beanie import Document
from pydantic import BaseModel, EmailStr


class Marker(Document):
    address: str
    category: Category
    lat: str
    lng: str
    comments: list[dict['userId': str, "comment": str, "date": str]]
    dumbBells: float  # 0-5

    class Settings:
        name = "markers"
