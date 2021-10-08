class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

def find_ID(name, info):
    if name in info:
        return info[name]
    raise StudentInfoError("Student ID not found for " + name)

def find_name(ID, info):
    for name in info:
        if ID == info[name]:
            return name
    raise StudentInfoError("Student name not found for " + ID)
