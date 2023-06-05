# Python_viestitulostin

Tekijät: Pinja Auer, Mikko Auvinen

Projektissa on käytetty FPDF-nimistä kirjastoa (versio 1.7.2). Lisää tietoa kirjastosta ja sen asentamisesta
löytyy osoitteesta https://pypi.org/project/fpdf/. Yksinkertaisesti tämä asennus tapahtuu kirjoittamalla Windows Powershellin komento "py -m pip install fpdf" (jos pip on ajantasalla).

FPDF:n lisäksi käytimme nimenomaan Python 3.11.3:sta.

Notes:

- FPDF käyttäytyi eri ympäristöissä eri tavalla, vaikka oli sama Python-versio ja sama FPDF-versio.
- Lähettäjä-kenttä ei suostunut mitenkään toimimaan kunnolla, kun alignmentiksi oltiin laitettu C (center) tai L (left), vaan FPDF halusi aina laittaa sen oikeaan reunaan puoliksi ulos dokumentista. R-alignmentin kanssa ei ollut mitään ongelmaa, mikä ei sinänsä haittaa koska lähettäjän nimi oikealla toimii.
