import PyPDF2


pdf_path = r"C:\Users\ae\Documents\devops.pdf"
pdf_file = open(pdf_path, "rb")

reader = PyPDF2.PdfFileReader(pdf_file)

print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())
pdf_file.close()
