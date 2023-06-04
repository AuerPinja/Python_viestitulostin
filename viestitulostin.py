from fpdf import FPDF


pdf = FPDF()  

pdf.add_page()

viesti = input("Kirjoita viesti: ")
lahettaja = input("Kirjoita lähettäjän nimi: ")

'''
color = input("Anna tekstin väri (sininen, punainen tai vihreä): ")


if color == "sininen":
    color = 0,0,255
elif color == "punainen":
    color = 255,0,0
elif color == "vihreä":
    color = 0,255,0
else: 
    print("Väriä ei ole saatavilla! Saatavilla olevat värit ovat sininen, punainen tai vihreä.")
'''



color = 255, 0, 0

pdf.set_font('Courier', size=30)
pdf.set_text_color(color)

pdf.cell(txt=viesti)
pdf.cell(txt=" ")
pdf.cell(txt="Terveisin: " + lahettaja)

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")
print("Viesti on tulostettu, ja se löytyy samasta kansiosta kuin tämä ohjelma.")