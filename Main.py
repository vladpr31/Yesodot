from Functions import Signup
from Functions import Login
from Functions import add_exam
from Functions import add_question
from Functions import Search
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
    print(Search())
elif Myclearance == 3:
    option = input("(1) Search\n\r(2) add exam\n\r(3) add question")
    if option == '1':
         print(Search())
    elif option == '2':
       ExamDataBase.append(add_exam())
    elif option == '3':
       QuestionDataBase.append(add_question())