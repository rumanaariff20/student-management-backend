from repositories.student_repository import (
    get_all_students,
    get_recent_students,
    add_student,
    update_student,
    delete_student,
    get_student_by_id,
    get_stats,
    get_departments,
)


def get_students(department=None, search=None):
    return get_all_students(department, search)

def recent_students():
    return get_recent_students()

def create_student(student):
    return add_student(student.model_dump())


def edit_student(student_id, student):
    data = student.model_dump(exclude_none=True)
    return update_student(student_id, data)


def remove_student(student_id):
    success = delete_student(student_id)

    if success:
        return {"message": "Student Deleted Successfully"}

    return {"message": "Student Not Found"}


def get_one_student(student_id):
    student = get_student_by_id(student_id)

    if student:
        return student

    return {"message": "Student Not Found"}


def student_stats():
    return get_stats()


def department_stats():
    return get_departments()