from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["StudentManagement"]

def get_students_collection():
    return db["Students"]