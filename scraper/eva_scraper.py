from bs4 import BeautifulSoup

class EvaScraper:
    def __init__(self):
        pass

    def parse_dump_file(self, html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        
        # TEMP: return dummy data until we wire real parsing logic
        return [
            {
                "title": "Example Opportunity",
                "agency": "Virginia Department of Transportation",
                "date": "2024-04-01",
                "url": "https://example.com/opportunity/123",
            }
        ]
