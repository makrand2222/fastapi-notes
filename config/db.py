import os

from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://makrandmandhare:f2uO4TUzUXeQ8TGH@fastapi.hdfdzwv.mongodb.net/notes")

conn = MongoClient(
    MONGO_URL
)
