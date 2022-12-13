import pyttsx3
import PyPDF2 

book = open('maas_paper.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Pages =", pages)
#for i in range(2, pages):
speaker = pyttsx3.init()
page = pdfReader.getPage(2)
text = page.extractText()
print("Text", end = "\n")
print(text)
speaker.say(text)
speaker.runAndWait()


