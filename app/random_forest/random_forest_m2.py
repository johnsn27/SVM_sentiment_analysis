import pickle
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorise(data, tfidf_vectorizer_fitted):
    """"Vectorise the data"""
    tfidf = tfidf_vectorizer_fitted.transform(data)
    words = tfidf_vectorizer_fitted.get_feature_names()
    tfidf_df = pd.DataFrame(tfidf.toarray())
    tfidf_df.columns = words
    return tfidf_df


def test_model(rf_classifier, a_val, b_val):
    """"Test the accuracy, precision and recall of the random forest model printing the results"""
    predict = rf_classifier.predict(a_val)
    f1_score = round(recall_score(b_val, predict, average='micro'), 3)

    print('f1', f1_score)


def create_model():
    """Create a random forest model"""
    dataset = pd.read_csv('../data/testRF.csv')

    sentiment = 'Label'
    text = 'Content'
    features = dataset.drop(sentiment, axis=1)
    labels = dataset[sentiment]

    a_train, a_test, b_train, b_test = \
        train_test_split(features, labels, test_size=0.90, random_state=42)
    a_train, a_test, b_train, b_test = \
        train_test_split(a_train, b_train, test_size=0.5, random_state=42)
    a_val, a_test, b_val, b_test = \
        train_test_split(a_test, b_test, test_size=0.5, random_state=42)

    tfidf_vectorizer = TfidfVectorizer(min_df=5,
                                       max_df=0.8,
                                       strip_accents='ascii',
                                       lowercase=True,
                                       use_idf=True)

    tfidf_vectorizer_fit = tfidf_vectorizer.fit(a_train[text])
    a_train = vectorise(a_train[text], tfidf_vectorizer_fit)

    a_val = vectorise(a_val[text], tfidf_vectorizer_fit)

    rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None)
    rf_classifier.fit(a_train, b_train.values.ravel())

    test_model(rf_classifier, a_val, b_val)

    pickle.dump(a_train, open('../models/train_data_RF.sav', 'wb'))
    pickle.dump(rf_classifier, open('../models/classifierRF.sav', 'wb'))


if __name__ == '__main__':
    create_model()