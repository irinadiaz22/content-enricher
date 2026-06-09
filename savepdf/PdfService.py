from fontTools.misc.cython import returns
from fpdf import FPDF

class PdfService:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto= True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_title(self, title: str):
        self.pdf.set_font("Arial", style= "B", size=16)
        self.pdf.cell(O, 10, title, ln=True, align="C")
        self.pdf.ln(5)
        self.pdf.set_font("Arial", size=12)

    def add_paragraph(self, text: str):
        self.pdf.multi_cell(0, 10, text)
        self.pdf.ln(5)

    def save(self, filename: str):
        self.pdf.output(filename)
        return filename

