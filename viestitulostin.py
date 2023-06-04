from fpdf import FPDF


pdf = FPDF()  

pdf.add_page()
  
pdf.set_font('Courier', size=30)

viesti = input("Kirjoita viesti: ")
lahettaja = input("Kirjoita lähettäjän nimi: ")

pdf.cell(txt=viesti, align = 'c')
pdf.cell(txt="Terveisin: " + lahettaja)

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")
print("Viesti on tulostettu, ja se löytyy samasta kansiosta kuin tämä ohjelma.")