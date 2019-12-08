class Person:
    def __init__(self, name, username, password, clearance):
        self.name = name
        self.username = username
        self.password = password
        self.clearance = clearance  # student\teacher\coordinator


class Student(Person):
    def __init__(self, name, username, password, clearance, year):
        super().__init__(name, username, password, clearance)
        self.year = year


class Staff(Person):
    def __init__(self, name, username, password, clearance, subject):
        super().__init__(name, username, password, clearance)
        self.subject = subject


def Signup():
    option = input("Choose:\n\r(1)Student (2)Teacher (3)Coordinator\n\r")
    if option == '1':
        name = input("Name:\n\r")
        username = input("Username:\n\r")
        password = input("Password:\n\r")
        year = input("Year:\n\r")
        newStudent = Student(name, username, password, 1, year)
        return newStudent
    elif option == '2':
        name = input("Name:\n\r")
        username = input("Username:\n\r")
        password = input("Password:\n\r")
        subject = input("Subject:\n\r")
        newTeacher = Staff(name, username, password, 2, subject)
        return newTeacher
    elif option == '3':
        name = input("Name:\n\r")
        username = input("Username:\n\r")
        password = input("Password:\n\r")
        subject = input("Subject:\n\r")
        newCoordinator = Staff(name, username, password, 3, subject)
        return newCoordinator

# main
PersonDataBase = []
PersonDataBase.append(Signup())
PersonDataBase.append(Signup())
print(PersonDataBase[0].name, PersonDataBase[1].name)