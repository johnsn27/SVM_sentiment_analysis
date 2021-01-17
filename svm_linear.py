import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

import pandas as pd


def train_model():
    train_data = pd.read_csv("data/train.csv")

    test_data = pd.read_csv("data/test.csv")

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=0.8,
                                 sublinear_tf=True,
                                 strip_accents='ascii',
                                 lowercase=True,
                                 use_idf=True)

    train_vectors = vectorizer.fit_transform(train_data['Content'])
    test_vectors = vectorizer.transform(test_data['Content'])

    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    classifier_linear.fit(train_vectors, train_data['Label'])
    prediction_linear = classifier_linear.predict(test_vectors)

    # results
    print("Results for SVC(kernel=linear)")
    report = classification_report(test_data['Label'], prediction_linear, output_dict=True)
    print('positive: ', report['pos'])
    print('negative: ', report['neg'])

    pickle.dump(vectorizer, open('models/vectorizer.sav', 'wb'))
    pickle.dump(classifier_linear, open('models/classifier.sav', 'wb'))
