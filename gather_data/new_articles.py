import time
from csv import reader

import os
import requests
from bs4 import BeautifulSoup as bs


class BBCArticle:
    """Class used to represent a BBC Article"""

    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()
        self.headline = self.get_headline()

    def get_body(self) -> list:
        """returns a list of the paragraphs in an article"""
        body = self.soup.find("article")
        return [p.text for p in body.find_all("p")]

    def get_headline(self) -> list:
        """returns a list of the headlines in an article"""
        body = self.soup.find("article")
        return [p.text for p in body.find_all("h1")]


def read_csv():
    """read the url from the published article csv"""
    file_path = os.path.abspath("news_csv_files/news_2019-07.csv")
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        i = 0
        for row in csv_reader:
            if i > 3000:
                break
            if i > 2500:
                url = "https://www.bbc.co.uk" + row[1]
                write_csv(url)
                time.sleep(1.1)
            i += 1


def write_csv(url):
    """write text of article to bbcArticles.txt file"""
    parsed = BBCArticle(url)
    parsed_str = str(parsed.body[1:-3])
    parsed_body = parsed_str[2:-2]
    file_path = os.path.abspath("datasets/bbcArticles.txt")
    file = open(file_path, "a")
    if parsed_body:
        file.write('\n' + parsed_body)
    file.close()


if __name__ == '__main__':
    read_csv()
