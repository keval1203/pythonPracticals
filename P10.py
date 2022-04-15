from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

Uni_result = PdfFileReader(str("C:\Users\keval\PycharmProjects\pythonProject\D21CS107"))
print(Uni_result.getDocumentInfo())
print(Uni_result.getNumPages())

for page in Uni_result.pages:
    print(page.extractText())
    PdfFileWriter().addPage(page)

with Path("C:\Users\keval\PycharmProjects\pythonProject\D21CS107").open("wb") as output:
    PdfFileWriter().write(output)