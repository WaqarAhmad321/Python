from PyPDF2 import PdfWriter
import os
merger = PdfWriter()

files = os.listdir("D:\\Code\\Python\\Modules\\Os Module\\cluttered")

for pdf in files:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("D:\\Code\\Python\\Modules\\Os Module\\pdf\\merged-pdf")
merger.close()
