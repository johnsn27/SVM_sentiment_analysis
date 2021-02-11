from csv import reader, writer
from app.fast_response_sentiment import fast_response_sentiment

import os


class ArticleWithSentiment:
    def __init__(self, sentiment, topic, text):
        self.sentiment = sentiment
        self.topic = topic
        self.text = text

    def print_sentiment(self):
        print("My sentiment is: " + self.sentiment)


def get_article_text(path="app/datasets/testArticles.csv"):
    """returns the text of an article"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            return row[0]


def article_url(path="app/datasets/testArticles.csv"):
    """read the url from the published article csv"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            url = row[0]
            return url


def create_article_with_sentiment():
    """read the url from the published article csv"""
    sentiment = fast_response_sentiment("text")
    url = article_url()
    text = get_article_text()
    article_with_sentiment = ArticleWithSentiment(sentiment, url, text)
    return article_with_sentiment


def write_to_dataset(path="app/datasets/bbc_articles_with_sentiment.csv"):
    """write text of article to bbcArticles.txt file"""
    article_with_sentiment = create_article_with_sentiment()
    with open(path, mode='a') as articles_with_sentiment_dataset:
        articles_writer = writer(articles_with_sentiment_dataset, delimiter=',')
        row = article_with_sentiment.sentiment, article_with_sentiment.topic, article_with_sentiment.text
        print('article_with_sentiment.sentiment', article_with_sentiment.sentiment)
        articles_writer.writerow(row)
