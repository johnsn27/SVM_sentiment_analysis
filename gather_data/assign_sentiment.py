import time
from csv import reader

import os


def read_csv():
    """read the text from the published article dataset"""
    file_path = os.path.abspath("datasets/bbcArticles.txt")
    with open(file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        # for row in csv_reader:
