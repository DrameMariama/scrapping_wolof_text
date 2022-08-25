import PyPDF2
import re

def read_pdf(filename):
    pdfobj = open(filename, "rb")
    pdf = PyPDF2.PdfFileReader(pdfobj)
    print(pdf.numPages)
    txt_filename = filename.split(".")[0]+".txt"
    with open(txt_filename, "w") as file:
        for i in range(pdf.numPages):
            page = pdf.getPage(i)
            text = page.extractText()
            text = re.sub("\d.", "", text)
            text = text.lstrip(".")
            text = text.strip()
            file.write(text)
            file.write("\n")
    pdfobj.close()


if __name__=="__main__":
    files = ["wol.pdf", "koor-wolof.pdf"]
    for filename in files:
        read_pdf(filename)