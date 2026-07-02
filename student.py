students = []

def add_student(name, student_id):
    students.append({'name': name, 'student_id': student_id})

def search_student(student_id):
    for s in students:
        if s['student_id'] == student_id:
            return s
    return None
