from translator.TranslatorService import TranslatorService
from scraper.ScraperWikipedia import ScraperWikipedia
from ai.GeminiAIService import GeminiAIService
from savepdf.PdfService import PdfService
from utils.utils import get_user_input

text = get_user_input("Ingresa el tema que quieres buscar: ")
src_lang = "auto"
trg_lang = get_user_input("Ingresa el idioma al que quieres traducir: ")

#Instancia la clase para buscar info de un tema en Wiquipedia
scraper = ScraperWikipedia(text)
enriched_service = GeminiAIService()

try:
    html = scraper.fetch_html()
    data = scraper.parse_html(html)

    print("Titulo: ",data["title"])
    print("Información encontrada")
    texto = data["paragraphs"]

    enriched = enriched_service.enrich_text(texto)
    print(f"Información enriquecida: {enriched}")
    translator = TranslatorService().translate_text(enriched, src_lang, trg_lang)
    print(translator)
    pdf = PdfService()
    pdf.add_title(data["title"])
    pdf.add_paragraph(enriched)
    pdf.save(text)

except Exception as e:
    print(f"Error encontrado: {e}")

