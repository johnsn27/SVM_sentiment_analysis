import time
from csv import reader, writer

import os


class ArticleWithSentiment:
    def __init__(self, sentiment, topic, text):
        self.sentiment = sentiment
        self.topic = topic
        self.text = text

    def print_sentiment(self):
        print("My sentiment is: " + self.sentiment)


def read_csv(path="../datasets/bbcArticles.csv"):
    """read the url from the published article csv"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            article_with_sentiment = ArticleWithSentiment("pos", row[0], "article text")
            write_csv(article_with_sentiment)


def write_csv(article_with_sentiment, path="../datasets/bbc_articles_with_sentiment.csv"):
    """write text of article to bbcArticles.txt file"""
    with open(path, mode='a') as articles_with_sentiment_dataset:
        articles_writer = writer(articles_with_sentiment_dataset, delimiter=',')
        row = article_with_sentiment.sentiment, article_with_sentiment.topic, article_with_sentiment.text
        print('article_with_sentiment.sentiment', article_with_sentiment.sentiment)
        articles_writer.writerow(row)

aws = ArticleWithSentiment("pos", "topic", "article text")
aws.print_sentiment()
read_csv()
