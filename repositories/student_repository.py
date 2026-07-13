from datetime import datetime
from database import get_students_collection

student_collection = get_students_collection()

def serialize(student):
    return {
        "id": str(student["_id"]),
        "name": student.get("name"),
        "age": student.get("age"),
        "department": student.get("department"),
        "email": student.get("email", ""),
        "phone": student.get("phone", ""),
        "createdAt": str(student.get("createdAt", "")),
    }


def get_all_students(department=None, search=None):
    query = {}

    if department:
        query["department"] = department

    if search:
        query["name"] = {
            "$regex": search,
            "$options": "i"
        }

    students = []

    for student in student_collection.find(query).sort("name", 1):
        students.append(serialize(student))

    return students

def get_recent_students(limit=5):

    students = []

    for student in student_collection.find().sort("createdAt", -1).limit(limit):
        students.append(serialize(student))

    return students

def get_student_by_id(student_id):
    from bson import ObjectId

    student = student_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student:
        return serialize(student)

    return None


def add_student(student):
    student["createdAt"] = datetime.utcnow()

    result = student_collection.insert_one(student)

    student = student_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize(student)


def update_student(student_id, data):
    from bson import ObjectId

    student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {
            "$set": data
        }
    )

    student = student_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student:
        return serialize(student)

    return None


def delete_student(student_id):
    from bson import ObjectId

    result = student_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    return result.deleted_count > 0


def get_stats():

    total = student_collection.count_documents({})

    departments = student_collection.distinct("department")

    pipeline = [
        {
            "$group": {
                "_id": None,
                "avgAge": {
                    "$avg": "$age"
                }
            }
        }
    ]

    avg = list(student_collection.aggregate(pipeline))

    average_age = round(avg[0]["avgAge"], 1) if avg else 0

    newest = student_collection.find_one(
        sort=[("createdAt", -1)]
    )

    return {
        "totalStudents": total,
        "totalDepartments": len(departments),
        "averageAge": average_age,
        "newestStudent": newest["name"] if newest else None
    }


def get_departments():

    pipeline = [
        {
            "$group": {
                "_id": "$department",
                "count": {
                    "$sum": 1
                },
                "averageAge": {
                    "$avg": "$age"
                }
            }
        }
    ]

    rows = list(student_collection.aggregate(pipeline))

    return [
        {
            "department": r["_id"],
            "count": r["count"],
            "averageAge": round(r["averageAge"], 1)
        }
        for r in rows
    ]