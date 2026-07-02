results = []

def add_result(student_id, score):
    results.append({'student_id': student_id, 'score': score})

def get_results():
    return results
