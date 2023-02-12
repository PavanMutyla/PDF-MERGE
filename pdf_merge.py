from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ['dummy.pdf','twopage.pdf']:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()