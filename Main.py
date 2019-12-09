from Functions import Signup
from Functions import Login
from Functions import add_exam
from Functions import add_question
from Functions import Search
from Functions import History
from Functions import Ticket
from Functions import ViewTickets
from Functions import Difficulty

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
    i = 0
    while i == 0:
        option = input("(1) Search\n\r(2) add difficulty\n\r")
        if option == '1':
            print(Search())
        elif option == '2':
            Difficulty()
elif Myclearance == 3:
    option = input("(1) Search\n\r(2) add exam\n\r(3) add question\n\r(4) Search History\n\r(5) Open ticket\n\r(6) "
                   "View tickets")
    if option == '1':
        print(Search())
    elif option == '2':
        ExamDataBase.append(add_exam())
    elif option == '3':
        QuestionDataBase.append(add_question())
    elif option == '4':
        print(History())
    elif option == '5':
        Ticket()
    elif option == '6':
        print(ViewTickets())
