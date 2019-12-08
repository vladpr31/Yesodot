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
    f = open("LoginCred.txt", "a")
    option = input("Choose:\n\r(1)Student (2)Teacher (3)Coordinator\n\r")
    if option == '1':
        name = input("Name:\n\r")
        f.write("Student_Name: " + name + "\n\r")
        username = input("Username:\n\r")
        f.write("Username: " + username + "\n\r")
        password = input("Password:\n\r")
        f.write("Password: " + password + "\n\r")
        year = input("Year:\n\r")
        f.write("Year: " + year + "\n\n\r")
        newStudent = Student(name, username, password, "Student", year)
        f.close()
        return newStudent
    elif option == '2':
        f = open("LoginCred.txt", "a")
        name = input("Name:\n\r")
        f.write("Tutor_Name: " + name + "\n\r")
        username = input("Username:\n\r")
        f.write("Username: " + username + "\n\r")
        password = input("Password:\n\r")
        f.write("Password: " + password + "\n\r")
        subject = input("Subject:\n\r")
        f.write("Teaching Subject: " + subject + "\n\n\r")
        newTeacher = Staff(name, username, password, 2, subject)
        f.close()
        return newTeacher
    elif option == '3':
        f = open("LoginCred.txt", "a")
        name = input("Name:\n\r")
        f.write("Tutor_Name: " + name + "\n\r")
        username = input("Username:\n\r")
        f.write("Username: " + username + "\n\r")
        password = input("Password:\n\r")
        f.write("Password: " + password + "\n\r")
        subject = input("Subject:\n\r")
        f.write("Teaching Subject: " + subject + "\n\n\r")
        newCoordinator = Staff(name, username, password, 3, subject)
        f.close()
        return newCoordinator

