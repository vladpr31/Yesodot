import File
from Exam import Exam
from Question import Question


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
