from fpdf import FPDF

pdf = FPDF()  

pdf.add_page()
  
pdf.set_font('Courier', size=30)

viesti = input("Kirjoita viesti: ")
pdf.multi_cell(ln = 1, txt=viesti, align = 'c')

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")