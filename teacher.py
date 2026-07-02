teachers = []

def add_teacher(name, subject):
    teachers.append({'name': name, 'subject': subject})

def search_teacher(name):
    for t in teachers:
        if t['name'] == name:
            return t
    return None
