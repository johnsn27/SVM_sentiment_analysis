import time
from csv import reader, writer, QUOTE_MINIMAL

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
    """read the url from the published article csv """
    file_path = os.path.abspath("../news_csv_files/news_2019-07.csv")
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        i = 0
        for row in csv_reader:
            if i > 2501:
                break
            if i > 2500:
                write_csv(row)
                time.sleep(1.1)
            i += 1


def write_csv(row):
    """write text of article to bbcArticles.txt file"""
    url_without_id = row[1].rsplit("-", 1)[0]
    topic = url_without_id.split("/")[2]
    print('topic', topic)
    url = "https://www.bbc.co.uk" + row[1]
    parsed = BBCArticle(url)
    paragraph1 = clean(str(parsed.body[2]))
    paragraph2 = clean(str(parsed.body[3]))
    paragraph3 = clean(str(parsed.body[4]))
    paragraph4 = clean(str(parsed.body[5]))
    rest_of_article = str(parsed.body[6:-3])
    file_path = os.path.abspath("../datasets/testArticles.csv")
    with open(file_path, mode='a') as articles_dataset:
        articles_writer = writer(articles_dataset, delimiter=',')
        articles_writer.writerow([topic, paragraph1, paragraph2, paragraph3, paragraph4, rest_of_article])


def clean(str_to_clean):
    return str_to_clean.translate({ord(char): None for char in '"'})


if __name__ == '__main__':
    read_csv()
