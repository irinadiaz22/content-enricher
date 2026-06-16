import pytest
from utils.CleanText import clean_text

def test_cleanText():
    texto = "Ecuador es miembro de la Comunidad Andina [1][2][5]**--"
    resultado = clean_text(texto)
    assert resultado == "Ecuador es miembro de la Comunidad Andina "
