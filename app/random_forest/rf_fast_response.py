import pickle
from flask import jsonify, make_response


def fast_response(text):
    """load a response from the saved trained model"""
    vectorizer = pickle.load(open('../models/vectorizerRF.sav', 'rb'))
    classifier = pickle.load(open('../models/classifierRF.sav', 'rb'))
    if text:
        text_vector = vectorizer.transform([text])
        result = classifier.predict(text_vector)
        new_data = result[0]
        print('new_data', new_data)
    #     with open('../document.csv', 'a') as new_data_document:
    #         new_data_document.write(new_data)
    #     return (
    #         make_response(
    #             jsonify({'sentiment': result[0], 'text': text, 'status_code': 200}), 200)
    #     )
    # return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)


if __name__ == '__main__':
    fast_response("bad")
