import pickle
from flask import jsonify, make_response


def fast_response_sentiment(text):
    """load a response from the saved trained model"""
    vectorizer = pickle.load(open('app/models/vectorizer.sav', 'rb'))
    classifier = pickle.load(open('app/models/classifier.sav', 'rb'))
    text_vector = vectorizer.transform([text])
    result = classifier.predict(text_vector)
    print('result', result)
    return result[0]
