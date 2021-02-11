import os

from csv import reader, writer
from app.fast_response_sentiment import fast_response_sentiment


class ArticleWithSentiment:
    """A class to represent an article with a sentiment rating

    Attributes:
        sentiment: sentiment rating for an article
        topic: topic of article
        text: full text of article
    """
    def __init__(self, sentiment, topic, text):
        """"Inits ArticleWithSentiment class with the sentiment, topic and text"""
        self.sentiment = sentiment
        self.topic = topic
        self.text = text

    def get_sentiment(self):
        """returns the sentiment of a given article"""
        return self.sentiment

    def get_topic(self):
        """returns the topic of a given article"""
        return self.topic

    def get_text(self):
        """returns the text of a given article"""
        return self.text


def get_article_text(path="app/datasets/testArticles.csv"):
    """returns the text of an article"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r') as read_obj:
        i = 0
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if i > 0:
                p1 = row[1]
                p2 = row[2]
                p3 = row[3]
                p4 = row[4]
                p5 = row[5]
                whole_article = p1 + p2 + p3 + p4 + p5
                return whole_article
            i += 1


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
    url = article_url()
    text = get_article_text()
    sentiment = fast_response_sentiment(text)
    article_with_sentiment = ArticleWithSentiment(sentiment, url, text)
    return article_with_sentiment


def write_to_dataset(path="app/datasets/bbc_articles_with_sentiment.csv"):
    """write text of article to bbcArticles.txt file"""
    article_with_sentiment = create_article_with_sentiment()
    with open(path, mode='a') as articles_with_sentiment_dataset:
        articles_writer = writer(articles_with_sentiment_dataset, delimiter=',')
        row = [article_with_sentiment.sentiment,
               article_with_sentiment.topic,
               article_with_sentiment.text]
        print('article_with_sentiment.sentiment', article_with_sentiment.sentiment)
        articles_writer.writerow(row)
