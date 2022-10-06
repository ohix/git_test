from fpdf import FPDF
from random_word import RandomWords
r = RandomWords()
r.get_random_word()



for i in range(1, 102):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(200, 10, txt="PoM[m]eS -  Gewinnspiel", ln=1, align="C")
    pdf.set_font("Helvetica", size=10)
    pdf.cell(200, 10, txt="Preise: Cafeteria-Gutschein | Süßigkeiten | 30-Sekunden Part im Podcast, mit jeder Audio die du uns zuschickst", ln=1, align="C")
    pdf.cell(200, 10, txt="Gib einfach diesen Code: " + r.get_random_word() + "-" + r.get_random_word() + " auf pomes.ml/code ein.", ln=1, align="C")
    pdf.cell(200, 10, txt="Gewinner werden im nächsten Podcast angekündigt!", ln=1, align="C")
    pdf.output("/Users/alex/Documents/the_odin_project/git_test/schule/python/pdf-generation/pommes-{}.pdf".format(i))

