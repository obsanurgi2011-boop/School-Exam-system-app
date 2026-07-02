admins = []

def add_admin(name, admin_id):
    admins.append({'name': name, 'admin_id': admin_id})

def search_admin(name):
    for a in admins:
        if a['name'] == name:
            return a
    return None
