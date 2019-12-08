class File:
    def __init__(self,subName,scndsubName,fformat,soltype):
        self.subjectName=subName
        self.secondSubName=scndsubName
        self.fileFormat=fformat
        self.solutiontype=soltype



F1=File("Math","Linear","Pdf","Partly")
print(F1.subjectName)
print(F1.secondSubName)
print(F1.fileFormat)
print(F1.solutiontype)


