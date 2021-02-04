import requests
from bs4 import BeautifulSoup as bs
from csv import reader
import time


class BBC:
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()

    def get_body(self) -> list:
        body = self.soup.find("article")
        return [p.text for p in body.find_all("p")]


def read_csv():
    with open('news_2019-07.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        i = 0
        for row in csv_reader:
            if i > 3000:
                break
            if i > 2500:
                print(str(i) + " " + 'https://www.bbc.co.uk' + row[1])
                url = "https://www.bbc.co.uk" + row[1]
                try:
                    parsed = BBC(url)
                    parsedStr = str(parsed.body[1:-3])
                    parsedBody = parsedStr[2:-2]
                    f = open("bbcArticles.txt", "a")
                    if parsedBody:
                        f.write('\n' + parsedBody)
                    f.close()
                    time.sleep(1.1)
                except:
                    pass
            i += 1


if __name__ == '__main__':
    read_csv()
