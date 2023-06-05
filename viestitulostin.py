from fpdf import FPDF
pdf = FPDF()
#Nämä rivit ottavat kirjaston käyttöön.

pdf.add_page()
#Tämä rivi luo sivun, jolle lisätä tekstiä.

otsikko = input("Kirjoita otsikko: ")
viesti = input("Kirjoita viesti: ")
lahettaja = input("Kirjoita lähettäjän nimi: ")
#Nämä rivit yksinkertaisesti syöttävät str-arvoja muuttujiin, jotta niitä voitaisiin myöhemmin käyttää funktioissa.

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
#Kaksi yksinkertaista while-looppia, joilla valitaan tekstin fontti ja väri useammasta etukäteen määritellystä vaihtoehdosta.

pdf.cell(0, 10, txt = otsikko, align = 'C', ln = 2)
pdf.cell(40, 10, '', ln = 2)
pdf.multi_cell(w = 0, h = 10, txt = viesti, align = 'L')
pdf.cell(0, 10, txt = "Terveisin: " + lahettaja)
#Nämä rivit luovat solut, joihin teksti syötetään. Rivillä 40 luotu solu jää tyhjäksi, koska se vain luo tasaisen välin otsikon
#ja varsinaisen viestin välille. Varsinaisen viestin solu(t) luodaan funktiolla multi_cell, eikä cell. Tällä tavalla ohjelma luo 
#allekkaisia soluja tarpeen mukaan, jos kaikki teksti ei mahdukaan yhteen soluun.

tiedosto = input("Anna viestillesi tiedostonimi: ")  
pdf.output(tiedosto+".pdf")
#Lopuksi käyttäjää pyydetään nimeämään uusi pdf-tiedosto.

print("Viesti on tulostettu, ja se löytyy samasta kansiosta kuin tämä ohjelma.")