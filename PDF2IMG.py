from pdf2jpg import pdf2jpg

x='C:/Users/VLAD/PycharmProjects/yesodot/outcome.pdf'
inputpath = x
outputpath = r"C:/Users/VLAD/PycharmProjects/yesodot/"
# To convert single page
result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="1")
print(result)