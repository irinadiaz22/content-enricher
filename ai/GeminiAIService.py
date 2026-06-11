import os
import time

from cffi import error
from google import genai
from dotenv import load_dotenv

load_dotenv()

class GeminiAIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("No se encuentra la GEMINI_API_KEY en el archivo .env")

        self.client = genai.Client(api_key=api_key)

    def enrich_text(self, text: str, retries: int = 3, delay: int = 2) -> str:
        prompt = f"Mejora y enriquece el siguiente texto manteniendo su , no me digas que mejoras hiciste, solo hazlas, Solo devuelveme el titulo y texto, sin escribir nada mas:\n\n{text}"
        for intento in range(1, retries + 1):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                if not response or not response.text:
                    raise ValueError("Sin respuesta de Gemini")

                return response.text

            except Exception as e:
                error.msg = str(e)

                if "503" in error.msg or "UNAVAILABLE" in error.msg:
                    print(f"Gemini respondio error 503 (intento {intento})/{retries}")
                    time.sleep(delay)
                    continue

                raise e     #si el error es distinto a 503, se lanza directamente
        raise RuntimeError("Gemini fallo después de varios intentos")




