import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class GeminiAIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("No se encuentra la GEMINI_API_KEY en el archivo .env")

        self.client = genai.Client(api_key=api_key)

    def enrich_text(self, text: str) -> str:
        prompt = f"Mejora y enriquece el siguiente texto manteniendo su significado:\n\n{text}"
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

