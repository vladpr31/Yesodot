from Question import Question
from Exam import Exam
from Student import Student
from Staff import Staff


def add_question():
    subName = input("Enter Question Subject:")
    scndsubName = input("Enter Question Sub-Subject:")
    fformat = input("Enter the Fomat(PDF or Word):")
    QuestionFile = input("Enter Question File:")  # entering the file PDF or Word
    solFile = input("Enter Solution File:")  # entering the file PDF or Word
    solType = input("Enter the Solution Type(Full,Partial,Final):")
    difficulty = input("Enter The Difficulty of the Question:")
    exam = input("Enter the Exam semester it was taken from:")
    newQuestion = Question(subName, scndsubName, fformat, QuestionFile, solFile, solType, difficulty, exam)
    return newQuestion


def add_exam():
    semester = input("Enter the Semester:")
    subName = input("Enter Exam Subject:")
    fformat = input("Enter the Fomat(PDF or Word):")
    examFile = input("Enter Exam File:")  # entering the file PDF or Word
    solFile = input("Enter Solution File:")  # entering the file PDF or Word
    solType = input("Enter the Solution Type(Full,Partial,Final):")
    newExam = Exam(semester, solFile, examFile, fformat, subName, solType)
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
