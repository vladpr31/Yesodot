from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger

pdf_file = PdfFileReader(open("C:/Users/VLAD/PycharmProjects/yesodot/1.pdf","rb"))
page = pdf_file.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

with open("1.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (10, 10)
        page.trimBox.upperRight = (612,0)
        page.cropBox.lowerLeft = (0, 612)
        page.cropBox.upperRight = (600, 730) #(from bottom)
        output.addPage(page)

    with open("outcome.jpeg", "wb") as out_f:
        output.write(out_f)
