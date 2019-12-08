from Person import Person as Parent


class Student(Parent):
    def __init__(self, name, username, password, clearance, year):
        super().__init__(name, username, password, clearance)
        self.year = year
