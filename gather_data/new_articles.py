import time
from csv import reader, writer

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
    bbc_article = BBCArticle(url)
    bbc_article_body = bbc_article.body
    paragraphs = get_paragraphs(bbc_article_body)
    rest_of_article = get_rest_of_article(bbc_article_body)
    file_path = os.path.abspath("../datasets/testArticles.csv")
    with open(file_path, mode='a') as articles_dataset:
        articles_writer = writer(articles_dataset, delimiter=',')
        article = [topic,
                   paragraphs[0], paragraphs[1], paragraphs[2], paragraphs[3],
                   rest_of_article]
        articles_writer.writerow(article)


def get_rest_of_article(bbc_article):
    """gets the text of the rest of the article"""
    rest_of_article = str(bbc_article[6:-3])
    clean_rest_of_article = clean(rest_of_article)
    return clean_rest_of_article


def get_paragraphs(bbc_article):
    """gets the first 4 paragraphs of the article"""
    paragraph1 = clean(str(bbc_article[2]))
    paragraph2 = clean(str(bbc_article[3]))
    paragraph3 = clean(str(bbc_article[4]))
    paragraph4 = clean(str(bbc_article[5]))
    paragraphs = paragraph1, paragraph2, paragraph3, paragraph4
    return paragraphs


def clean(str_to_clean):
    """removes the " character from a string """
    return str_to_clean.translate({ord(char): None for char in '"'})


if __name__ == '__main__':
    read_csv()
