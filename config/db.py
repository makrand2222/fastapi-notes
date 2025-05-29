import os

from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", None)

conn = MongoClient(
    MONGO_URL
)
