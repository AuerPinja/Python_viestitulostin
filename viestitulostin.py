from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

otsikko = input("Kirjoita otsikko: ")
viesti = input("Kirjoita viesti: ")
lahettaja = input("Kirjoita lähettäjän nimi: ")

while True:
    fontti = input("Mikä fontti (Courier tai Arial)? ")
    if fontti == "Courier":
        pdf.set_font("Courier", size = 16)
        break
    elif fontti == "Arial":
        pdf.set_font("Arial", size = 16)
        break
    else:
        print("Valitsemaasi fonttia ei ole saatavilla.")

while True:
    color = input("Anna tekstin väri (sininen, punainen tai vihreä): ")
    if color == "sininen":
        pdf.set_text_color(0,0,255)
        break
    elif color == "punainen":
        pdf.set_text_color(255,0,0)
        break
    elif color == "vihreä":
        pdf.set_text_color(0,255,0)
        break
    else:
        print("Valitsemaasi väriä ei ole saatavilla")

pdf.cell(0, 10, txt = otsikko, align = 'C', ln = 2)
pdf.cell(40, 10, '', ln = 2)
pdf.multi_cell(w = 0, h = 10, txt = viesti, border = 0, align = 'L')
pdf.cell(0, 10, txt = "Terveisin: " + lahettaja)
#pdf.multi_cell(w = 0, h = 0, txt = viesti + "Terveisin: " + lahettaja)

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")
print("Viesti on tulostettu, ja se löytyy samasta kansiosta kuin tämä ohjelma.")