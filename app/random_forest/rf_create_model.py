import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import nltk
import pickle

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.feature_extraction.text import TfidfVectorizer
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

imdb = pd.read_csv('kaggle/input/Train.csv')

features = imdb.drop("label", axis=1)
labels = imdb["label"]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.90, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.5, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)


def vectorize(data, tfidf_vect_fit):
    X_tfidf = tfidf_vect_fit.transform(data)
    words = tfidf_vect_fit.get_feature_names()
    X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
    X_tfidf_df.columns = words
    return (X_tfidf_df)


tfidf_vect = TfidfVectorizer()
tfidf_vect_fit = tfidf_vect.fit(X_train['text'])
X_train = vectorize(X_train['text'], tfidf_vect_fit)

X_val = vectorize(X_val['text'], tfidf_vect_fit)

rf2 = RandomForestClassifier(n_estimators=100, max_depth=None)
rf2.fit(X_train, y_train.values.ravel())

y_pred = rf2.predict(X_val)
accuracy = round(accuracy_score(y_val, y_pred), 3)
precision = round(precision_score(y_val, y_pred), 3)
recall = round(recall_score(y_val, y_pred), 3)
print('MAX DEPTH: {} / # OF EST: {} -- A: {} / P: {} / R: {}'.format(rf2.max_depth,
                                                                     rf2.n_estimators,
                                                                     accuracy,
                                                                     precision,
                                                                     recall))

X_test = vectorize(X_test['text'], tfidf_vect_fit)

pickle.dump(X_train, open('../models/train_data_RF.sav', 'wb'))
pickle.dump(rf2, open('../models/classifierRF.sav', 'wb'))

