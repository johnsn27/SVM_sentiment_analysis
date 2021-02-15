import pickle
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = pd.read_csv('../data/trainRF.csv')

features = dataset.drop("label", axis=1)
labels = dataset["label"]

a_train, a_test, b_train, b_test = \
    train_test_split(features, labels, test_size=0.90, random_state=42)
a_train, a_test, b_train, b_test = \
    train_test_split(a_train, b_train, test_size=0.5, random_state=42)
a_val, a_test, b_val, b_test = \
    train_test_split(a_test, b_test, test_size=0.5, random_state=42)


def vectorise(data, tfidf_vectorizer_fitted):
    """"Vectorise the data"""
    tfidf = tfidf_vectorizer_fitted.transform(data)
    words = tfidf_vectorizer_fitted.get_feature_names()
    tfidf_df = pd.DataFrame(tfidf.toarray())
    tfidf_df.columns = words
    return tfidf_df


tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer_fit = tfidf_vectorizer.fit(a_train['text'])
a_train = vectorise(a_train['text'], tfidf_vectorizer_fit)

a_val = vectorise(a_val['text'], tfidf_vectorizer_fit)

rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None)
rf_classifier.fit(a_train, b_train.values.ravel())

b_pred = rf_classifier.predict(a_val)
accuracy = round(accuracy_score(b_val, b_pred), 3)
precision = round(precision_score(b_val, b_pred), 3)
recall = round(recall_score(b_val, b_pred), 3)


a_test = vectorise(a_test['text'], tfidf_vectorizer_fit)

pickle.dump(a_train, open('../models/train_data_RF.sav', 'wb'))
pickle.dump(rf_classifier, open('../models/classifierRF.sav', 'wb'))
