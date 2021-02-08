import pickle
from flask import jsonify, make_response


def fast_response(text):
    """load a response from the saved trained model"""
    vectorizer = pickle.load(open('app/models/vectorizer.sav', 'rb'))
    classifier = pickle.load(open('app/models/classifier.sav', 'rb'))
    if text:
        text_vector = vectorizer.transform([text])
        result = classifier.predict(text_vector)
        new_data = text + ", " + result[0] + "\n"
        with open('../document.csv', 'a') as new_data_document:
            new_data_document.write(new_data)
        return (
            make_response(
                jsonify({'sentiment': result[0], 'text': text, 'status_code': 200}), 200)
        )
    return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)
