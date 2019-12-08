from Person import Person as Parent


class Staff(Parent):
    def __init__(self, name, username, password, clearance, subject):
        super().__init__(name, username, password, clearance)
        self.subject = subject
