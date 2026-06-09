from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException, ServerException
class TranslatorService:
    #Método constructor siempre antes de una clase
    def __init__(self):
        pass
    def translate_text(self, text: str, source_lang: str, target_lang: str):
        try:
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            return translated_text
        except LanguageNotSupportedException as e:
            print(f"Idioma no soportado: {e}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")







