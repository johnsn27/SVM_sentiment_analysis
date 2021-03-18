# pylint: disable=missing-module-docstring#
# Remove R0801 from .pylintrc
# need to unduplicate code
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pandas as pd


def train_model():
    """redundant at this moment in time """

    train_data = pd.read_csv("./datasets/fine_dataset_train.csv")

    test_data = pd.read_csv("./datasets/fine_dataset_test.csv")

    # Create feature vectors
    vectorizer = TfidfVectorizer(analyzer='word',
                                 decode_error='strict',
                                 min_df=3,
                                 max_df=0.5,
                                 sublinear_tf=True,
                                 strip_accents='ascii',
                                 lowercase=True,
                                 use_idf=True)

    train_vectors = vectorizer.fit_transform(train_data['Content'].values.astype('U'))
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
    print('neutral: ', report['nr'])

    pickle.dump(vectorizer, open('models/vectorizer.sav', 'wb'))
    pickle.dump(classifier_linear, open('models/classifier.sav', 'wb'))


if __name__ == '__main__':
    train_model()
