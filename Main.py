from Functions import Signup
from Functions import Login


PersonDataBase = []
ExamDataBase = []
QuestionDataBase = []
Myclearance = 0
option = input("(1) Log in\n\r(2) Sign up\n\r")
if option == '1':
    Myclearance=Login()
else:
    PersonDataBase.append(Signup())
    print("Please log in:\n\r")
    Myclearance = Login()
if Myclearance == 1 or Myclearance == 2:
    Text = input("Search:\n\r")
else:
    option = input("(1) Search\n\r(2) add exam\n\r")