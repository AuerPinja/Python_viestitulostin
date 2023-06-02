'''
from fpdf import FPDF
# moi

print("Hello World!")

pdf = FPDF()  

pdf.add_page()
  
pdf.set_font('Courier', size=30)

viesti = input("Kirjoita viesti: ")
pdf.multi_cell(ln = 1, txt=viesti, align = 'c')

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf") 
'''

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

message = input("Enter your message: ")
tiedosto = input("Anna tiedostonimi: ")

wraped_text = "\n".join(wrap(message, 80))

pdf_file = tiedosto+".pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFillColorRGB(1,0,0)
c.setFont("Helvetica", 20)
c.drawString(100, 700, message)
c.save()

print("Viesti on tallennettu!")