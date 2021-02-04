import requests
from bs4 import BeautifulSoup as bs


class BBC:
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()

    def get_body(self) -> list:
        body = self.soup.find("article")
        return [p.text for p in body.find_all("p")]


url = "https://www.bbc.co.uk/news/education-48804395"
try:
    parsed = BBC(url)
    parsedStr = str(parsed.body[1:-3])
    parsedBody = parsedStr[2:-2]
    f = open("bbcArticles.txt", "a")
    if parsedBody:
        f.write('\n' + parsedBody)
    f.close()
except:
    pass
