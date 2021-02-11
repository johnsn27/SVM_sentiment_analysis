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


def read_csv(path="app/datasets/testArticles.csv"):
    """read the url from the published article csv"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            sentiment = fast_response_sentiment("text")
            article_with_sentiment = ArticleWithSentiment(sentiment, row[0], "article text")
            write_csv(article_with_sentiment)


def write_csv(article_with_sentiment, path="app/datasets/bbc_articles_with_sentiment.csv"):
    """write text of article to bbcArticles.txt file"""
    with open(path, mode='a') as articles_with_sentiment_dataset:
        articles_writer = writer(articles_with_sentiment_dataset, delimiter=',')
        row = article_with_sentiment.sentiment, article_with_sentiment.topic, article_with_sentiment.text
        print('article_with_sentiment.sentiment', article_with_sentiment.sentiment)
        articles_writer.writerow(row)
