from fastapi import APIRouter, Query
from typing import Optional

from models.student_model import StudentInput, StudentUpdate

from services.student_service import (
    get_students,
    recent_students,
    create_student,
    edit_student,
    remove_student,
    get_one_student,
    student_stats,
    department_stats,
)

router = APIRouter(prefix="/api/students", tags=["Students"])


# GET /api/students/stats
@router.get("/stats")
def stats():
    return student_stats()


# GET /api/students/departments
@router.get("/departments")
def departments():
    return department_stats()

# GET /api/students/recent
@router.get("/recent")
def recent():
    return recent_students()


# GET /api/students
@router.get("")
def read_students(
    department: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
):
    return get_students(department, search)


# POST /api/students
@router.post("")
def add(student: StudentInput):
    return create_student(student)


# GET /api/students/{student_id}
@router.get("/{student_id}")
def read_one(student_id: str):
    return get_one_student(student_id)


# PUT /api/students/{student_id}
@router.put("/{student_id}")
def update(student_id: str, student: StudentUpdate):
    return edit_student(student_id, student)


# DELETE /api/students/{student_id}
@router.delete("/{student_id}")
def delete(student_id: str):
    return remove_student(student_id)