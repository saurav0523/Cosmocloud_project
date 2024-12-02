from motor.motor_asyncio import AsyncIOMotorClient

from .config import Settings

settings = Settings()

client = AsyncIOMotorClient(settings.DB_URL)
db = client.get_database("college")
students_collection = db.get_collection("students")  