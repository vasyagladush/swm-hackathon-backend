from beanie import Document


class DumbBell(Document):
    rating: float
    markerId: str
    userId: str

    class Settings:
        name = "dumbbells"