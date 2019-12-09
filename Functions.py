from random import randint
from Question import Question
from Exam import Exam
from Student import Student
from Staff import Staff
import sys

def add_question():
    def idcheck():
        i = 0
        while i == 0:
            id = randint(10000, 99999)
            with open("QuestionBank.txt") as g:
                if str(id) in g.read():
                    pass
                else:
                    i = 1
                    return id
    f = open("QuestionBank.txt", "a")
    myid = str(idcheck())
    subName = input("Enter Question Subject:")
    f.write("Subject: " + subName + " ")
    amount = int(input("How many paragraphs in the question?"))
    for i in range(amount):
        scndsubName = input("Enter paragraph subject #"+str(i+1)+":")
        f.write("Sub-Subject(" + str(i+1) +"):" + scndsubName + ", Difficulty: # ")
    fformat = input("Enter the Fomat(PDF or Word):")
    QuestionFile = input("Enter Question File:")  # entering the file PDF or Word
    solFile = input("Enter Solution File:")  # entering the file PDF or Word
    solType = input("Enter the Solution Type(Full,Partial,Final):")
    exam = input("Enter the Exam semester it was taken from:")
    f.write("Semester: " + exam + " ")
    f.write("Solution type: " + solType + "\n\r")
    f.write("ID: " + myid + "\n\r")
    newQuestion = Question(myid, subName, fformat, QuestionFile, solFile, solType, exam)
    f.close()
    return newQuestion


def add_exam():
    def idcheck():
        i = 0
        while i == 0:
            id = randint(10000, 99999)
            with open("QuestionBank.txt") as g:
                if str(id) in g.read():
                    pass
                else:
                    i = 1
                    return id

    f = open("ExamBank.txt", "a")
    myid = str(idcheck())
    f.write("ID: " + myid + " ")
    semester = input("Enter the Semester:")
    subName = input("Enter Exam Subject:")
    fformat = input("Enter the Fomat(PDF or Word):")
    examFile = input("Enter Exam File:")  # entering the file PDF or Word
    solFile = input("Enter Solution File:")  # entering the file PDF or Word
    solType = input("Enter the Solution Type(Full,Partial,Final):")
    f.write("Subject: " + subName + " ")
    f.write("Semester: " + semester + " ")
    newExam = Exam(myid, semester, solFile, examFile, fformat, subName, solType)
    f.close()
    return newExam


def Signup():
    def usercheck():
        i = 0
        while i == 0:
            user = input("Username:\n\r")
            with open("LoginCred.txt") as g:
                if "Username: "+user+" " in g.read():
                    print("Username taken, try again.\n\r")
                else:
                    i = 1
                    return user
    f = open("LoginCred.txt", "a")
    option = input("Choose:\n\r(1)Student (2)Teacher (3)Coordinator\n\r")
    if option == '1':
        name = input("Name:\n\r")
        f.write("Student_Name: " + name + " ")
        username = usercheck()
        f.write("Clearance: 1" + " ")
        f.write("Username: " + username + " ")
        password = input("Password:\n\r")
        f.write("Password: " + password + " ")
        year = input("Year:\n\r")
        f.write("Year: " + year + "\n\r")
        newStudent = Student(name, username, password, "Student", year)
        f.close()
        return newStudent
    elif option == '2':
        f = open("LoginCred.txt", "a")
        name = input("Name:\n\r")
        f.write("Tutor_Name: " + name + " ")
        username = input("Username:\n\r")
        f.write("Clearance: 2" + " ")
        f.write("Username: " + username + " ")
        password = input("Password:\n\r")
        f.write("Password: " + password + " ")
        subject = input("Subject:\n\r")
        f.write("Teaching Subject: " + subject + "\n\r")
        newTeacher = Staff(name, username, password, 2, subject)
        f.close()
        return newTeacher
    elif option == '3':
        f = open("LoginCred.txt", "a")
        name = input("Name:\n\r")
        f.write("Tutor_Name: " + name + " ")
        f.write("Clearance: 3" + " ")
        username = input("Username:\n\r")
        f.write("Username: " + username + " ")
        password = input("Password:\n\r")
        f.write("Password: " + password + " ")
        subject = input("Subject:\n\r")
        f.write("Teaching Subject: " + subject + "\n\r")
        newCoordinator = Staff(name, username, password, 3, subject)
        f.close()
        return newCoordinator


def Login():
    i = 0
    user = 0
    while i == 0:
        user = input("Username:\n\r")
        with open("LoginCred.txt") as g:
            if "Username: "+user not in g.read():
                print("Wrong username, try again.\n\r")
            else:
                i = 1
    i = 0
    while i == 0:
        password = input("Password:\n\r")
        with open("LoginCred.txt") as g:
            if "Username: "+user+" Password: "+password+" " not in g.read():
                print("Wrong password, try again.\n\r")
            else:
                i = 1
    print("Welcome "+user+"!\n\r")
    with open("LoginCred.txt") as g:
        if "Clearance: 1 Username: " + user + " " in g.read():
            return 1
        elif "Clearance: 2 Username: " + user + " " in g.read():
            return 2
        else:
            return 3


def Search():
    option = input("(1) Free search:\n\r(2) Search with options\n\r")
    if option == '1':
        KeyWord = input("Search: ")
        f = open("History.txt", "a")
        f.write(KeyWord + "\n\r")
        f.close()
        newstr = ''
        with open("QuestionBank.txt") as f:
            for line in f:
                if KeyWord in line:
                    mystr = f.readline(9)
                    newstr = newstr + mystr + "\n"
        return newstr
    elif option == '2':
        KeyWord = input("Search: ")
        f = open("History.txt", "a")
        f.write(KeyWord + "\n\r")
        f.close()
        KeyWord1 = input("Difficulty(1-5): ")
        KeyWord2 = input("Solution type(Full, Partial, Final): ")
        newstr = ''
        with open("QuestionBank.txt") as f:
            for line in f:
                if KeyWord and KeyWord1 and KeyWord2 in line:
                    mystr = f.readline(9)
                    newstr = newstr + mystr + "\n"
        return newstr


def OpenTicket():
    pass


def History():
    with open("History.txt", 'r') as f:
        return f.read()


def Ticket():
    f = open("Ticket.txt", "a")
    Mytext = input("Enter your text here:\n\r")
    f.write(Mytext + "\n\r")
    f.close()


def ViewTickets():
    with open("Ticket.txt", 'r') as f:
        return f.read()


def Difficulty():
    myid = input("Enter question ID:")
    par = input("Enter question paragraph")
    newdif = input("Enter Difficulty:")
    with open("QuestionBank.txt") as f:
        for line in f:
            if myid in line:
                line = line.replace("Sub-Subject("+par+"): Difficulty: #", "Sub-Subject("+par+"): Difficulty: "+newdif+"")
                
    print("Difficulty updated!\n\r")
