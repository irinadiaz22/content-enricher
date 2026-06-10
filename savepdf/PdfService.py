import os
from fpdf import FPDF

class PdfService:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto= True, margin=15)
        self.pdf.add_page()
        self.pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
        self.pdf.set_font("DejaVu",size=12)

    def add_title(self, title: str):
        self.pdf.set_font("Arial", style= "B", size=16)
        self.pdf.cell(w=0, h=10, txt=title, ln=True, align="C")
        self.pdf.ln(5)
        self.pdf.set_font("DejaVu",size=12)

    def add_paragraph(self, text: str):
        self.pdf.multi_cell(0, 10, text)
        self.pdf.ln(5)
        print("Generando pdf")

    def save(self, filename: str):
        nombre_archivo = input("Ingrese el nombre del archivo: (sin .pdf)")
        os.makedirs("output", exist_ok=True)
        ruta = f"output/{nombre_archivo}.pdf"
        self.pdf.output(ruta)
        print(f"PDF guardado en : {ruta}")
        return filename

