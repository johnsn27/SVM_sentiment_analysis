import pickle
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorise(data, tfidf_vectorizer_fitted):
    """"Vectorise the data"""
    tfidf = tfidf_vectorizer_fitted.transform(data)
    words = tfidf_vectorizer_fitted.get_feature_names()
    tfidf_df = pd.DataFrame(tfidf.toarray())
    tfidf_df.columns = words
    return tfidf_df


def create_model():
    dataset = pd.read_csv('../data/trainRF.csv')

    sentiment = "label"
    text = 'text'

    features = dataset.drop(sentiment, axis=1)
    labels = dataset[sentiment]


    a_train, a_test, b_train, b_test = \
        train_test_split(features, labels, test_size=0.90, random_state=42)
    a_train, a_test, b_train, b_test = \
        train_test_split(a_train, b_train, test_size=0.5, random_state=42)

    tfidf_vectorizer = TfidfVectorizer(min_df=5,
                                       max_df=0.8,
                                       strip_accents='ascii',
                                       lowercase=True,
                                       use_idf=True)

    tfidf_vectorizer_fit = tfidf_vectorizer.fit(a_train[text])
    a_train = vectorise(a_train[text], tfidf_vectorizer_fit)

    rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None)
    rf_classifier.fit(a_train, b_train.values.ravel())

    pickle.dump(a_train, open('../models/train_data_RF.sav', 'wb'))
    pickle.dump(rf_classifier, open('../models/classifierRF.sav', 'wb'))
