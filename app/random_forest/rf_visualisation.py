import pickle
import matplotlib.pyplot as plt
import pandas as pd


def get_list_of_most_extreme_words(num):
    train_data = pickle.load(open('../models/train_data_RF.sav', 'rb'))
    classifier = pickle.load(open('../models/classifierRF.sav', 'rb'))
    list_of_words = pd.Series(classifier.feature_importances_, index=train_data.columns)
    most_extreme_words = list_of_words.nlargest(num)
    return most_extreme_words.keys()


def rf_create_graph():
    """"Creates a bar chart of the most important features """
    get_list_of_most_extreme_words(20).plot(kind='bar', figsize=(10, 10))
    plt.title("Top 20 important features")
    plt.show()


def highlight_words(text):
    most_extreme_words = get_list_of_most_extreme_words(61)
    list_of_input_words = text.split(" ")
    words_to_highlight =[]
    for word in most_extreme_words:
        for inputted_word in list_of_input_words:
            if word == inputted_word:
                words_to_highlight.append(word)
    return words_to_highlight


if __name__ == '__main__':
    highlight_words("This was the worst, just awful")
