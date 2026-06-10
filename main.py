from translator.TranslatorService import TranslatorService
from scraper.ScraperWikipedia import ScraperWikipedia
from ai.GeminiAIService import GeminiAIService
from savepdf.PdfService import PdfService
from utils.utils import get_user_input
from utils.YesNoService import YesNoService

text = get_user_input("Ingresa el tema que quieres buscar: ")

#Instancia la clase para buscar info de un tema en Wiquipedia
scraper = ScraperWikipedia(text)
enriched_service = GeminiAIService()

try:
    html = scraper.fetch_html()
    data = scraper.parse_html(html)

    print("Titulo: ",data["title"])
    print("Información encontrada")
    texto = data["paragraphs"]
    print(texto)

    enriched = enriched_service.enrich_text(texto)
    print(f"Información enriquecida: \n {enriched}")

    src_lang = "auto"
    trg_lang = get_user_input("Ingresa el idioma al que quieres traducir: ")

    translator = TranslatorService().translate_text(enriched, src_lang, trg_lang)
    print(translator)
    txt_pdf = ""
    print("¿Que quieres agregar al documento PDF?")
    yn = YesNoService()
    if yn.ask("Añadir texto original: y/n"):
        txt_pdf = texto

    if yn.ask("Añadir texto enriquesido: y/n"):
        txt_pdf = (f"{txt_pdf} + \n + {enriched}")

    if yn.ask("Añadir texto traducido: y/n"):
        txt_pdf = (f"{txt_pdf} + \n + {translator}")

    pdf = PdfService()
    pdf.add_title(data["title"])
    pdf.add_paragraph(txt_pdf)
    pdf.save(text)

except Exception as e:
    print(f"Error encontrado: {e}")

