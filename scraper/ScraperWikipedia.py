import requests
from bs4 import BeautifulSoup

class ScraperWikipedia:
    BASE_URL = "https://es.wikipedia.org/wiki/"

    def __init__(self, topic: str):
        self.topic = topic.replace(" ", "_")
        self.url = self.BASE_URL + self.topic
        pass
    #método para descargar la pagina
    def fetch_html(self) -> str:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0 Safari/537.36"
            )
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text
    #buscar dentro del html
    def parse_html(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        #buscar los títulos con el texto que quiero
        title = soup.find("h1").text.strip()
        #Para trer los párrafos
        paragraphs = soup.find_all("p")
        get_five_paragraphs = [p.text.strip() for p in paragraphs[:5]]

        return {
            "title": title,
            "paragraphs": get_five_paragraphs
        }



