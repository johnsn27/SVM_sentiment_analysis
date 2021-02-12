import inline as inline
import matplotlib as matplotlib
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import re
import nltk

from sklearn.model_selection import GridSearchCV
from wordcloud import WordCloud
from collections import Counter
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
print(imdb.info())
print(imdb.shape)
print(imdb.head(10))


# Creates pie chart of positive vs negative
# imdb['label'].value_counts().plot.pie(figsize=(6, 6), title="Distribution of reviews per sentiment", labels=['', ''],
#                                       autopct='%1.1f%%')
# labels = ["Positive", "Negative"]
# plt.legend(labels, loc=3)
# plt.gca().set_aspect('equal')

features = imdb.drop("label", axis=1)
labels = imdb["label"]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.90, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.5, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

print("Data distribution:\n- Train: {} \n- Validation: {} \n- Test: {}".format(len(y_train), len(y_val), len(y_test)))


def clean(text):
    wn = nltk.WordNetLemmatizer()
    stopword = nltk.corpus.stopwords.words('english')
    tokens = nltk.word_tokenize(text)
    lower = [word.lower() for word in tokens]
    no_stopwords = [word for word in lower if word not in stopword]
    no_alpha = [word for word in no_stopwords if word.isalpha()]
    lemm_text = [wn.lemmatize(word) for word in no_alpha]
    clean_text = lemm_text
    return clean_text


imdb = imdb.head(1000)
print("Processing data...")
imdb['clean'] = imdb['text'].map(clean)
imdb['clean_text'] = imdb['clean'].apply(lambda x: " ".join([str(word) for word in x]))

positive_words = " ".join(imdb[imdb.label == 1]['clean_text'].values)
negative_words = " ".join(imdb[imdb.label == 0]['clean_text'].values)


def vectorize(data, tfidf_vect_fit):
    X_tfidf = tfidf_vect_fit.transform(data)
    words = tfidf_vect_fit.get_feature_names()
    X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
    X_tfidf_df.columns = words
    return (X_tfidf_df)


tfidf_vect = TfidfVectorizer(analyzer=clean)
tfidf_vect_fit = tfidf_vect.fit(X_train['text'])
X_train = vectorize(X_train['text'], tfidf_vect_fit)

rf = RandomForestClassifier()
scores = cross_val_score(rf, X_train, y_train.values.ravel(), cv=5)

print(scores)
scores.mean()


def print_results(results):
    print('BEST PARAMS: {}\n'.format(results.best_params_))

    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))


rf = RandomForestClassifier()
parameters = {
    'n_estimators': [5, 50, 100],
    'max_depth': [2, 10, 20, None]
}

cv = GridSearchCV(rf, parameters)
cv.fit(X_train, y_train.values.ravel())
print_results(cv)

cv.best_estimator_

X_val = vectorize(X_val['text'], tfidf_vect_fit)

rf1 = RandomForestClassifier(n_estimators=100, max_depth=20)
rf1.fit(X_train, y_train.values.ravel())
rf2 = RandomForestClassifier(n_estimators=100, max_depth=None)
rf2.fit(X_train, y_train.values.ravel())
rf3 = RandomForestClassifier(n_estimators=5, max_depth=None)
rf3.fit(X_train, y_train.values.ravel())

for mdl in [rf1, rf2, rf3]:
    y_pred = mdl.predict(X_val)
    accuracy = round(accuracy_score(y_val, y_pred), 3)
    precision = round(precision_score(y_val, y_pred), 3)
    recall = round(recall_score(y_val, y_pred), 3)
    print('MAX DEPTH: {} / # OF EST: {} -- A: {} / P: {} / R: {}'.format(mdl.max_depth,
                                                                         mdl.n_estimators,
                                                                         accuracy,
                                                                         precision,
                                                                         recall))

X_test = vectorize(X_test['text'], tfidf_vect_fit)

y_pred = rf2.predict(X_test)
accuracy = round(accuracy_score(y_test, y_pred), 3)
precision = round(precision_score(y_test, y_pred), 3)
recall = round(recall_score(y_test, y_pred), 3)
print('MAX DEPTH: {} / # OF EST: {} -- A: {} / P: {} / R: {}'.format(rf3.max_depth,
                                                                     rf3.n_estimators,
                                                                     accuracy,
                                                                     precision,
                                                                     recall))

feat_importances = pd.Series(rf2.feature_importances_, index=X_train.columns)
feat_importances.nlargest(20).plot(kind='bar', figsize=(10, 10))
print(feat_importances.nlargest(20))
plt.title("Top 20 important features")
plt.show()
