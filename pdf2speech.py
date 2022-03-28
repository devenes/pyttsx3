import pyttsx3
import PyPDF2


pdf_path = r"C:\Users\ae\Documents\devops.pdf"
pdf_file = open(pdf_path, "rb")

reader = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = reader.numPages

engine = pyttsx3.init()
for i in range(number_of_pages):
    page = reader.getPage(i)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
