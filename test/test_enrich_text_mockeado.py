from unittest.mock import patch, MagicMock
from ai.GeminiAIService import GeminiAIService

def test_enrich_text_mockeado():
    servicio = GeminiAIService()

    mock_response = MagicMock()
    mock_response.text = "Texto enriquecido"

    with patch.object(servicio.client.models, "generate_content", return_value=mock_response):
        resultado = servicio.enrich_text("Ecuador")

    assert resultado == "Texto enriquecido"
