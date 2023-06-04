from fpdf import FPDF


pdf = FPDF()  

pdf.add_page()

viesti = input("Kirjoita viesti: ")
lahettaja = input("Kirjoita lähettäjän nimi: ")

color = 255,35,97
  
pdf.set_font('Courier', size=30)
pdf.set_text_color(color)

pdf.cell(txt=viesti)
pdf.cell(txt=" ")
pdf.cell(txt="Terveisin: " + lahettaja)

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")
print("Viesti on tulostettu, ja se löytyy samasta kansiosta kuin tämä ohjelma.")