import pickle

from flask import Flask, jsonify, make_response, request
from svm_linear import train_model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

vectorizer = pickle.load(open('models/vectorizer.sav', 'rb'))
classifier = pickle.load(open('models/classifier.sav', 'rb'))


# todo: we want to use some of the model we already have
#  then also incorporate new data we are getting into the model
#  so that we don't have to do train_model() at the start of every run
#  this will help:
#  https://stackoverflow.com
#  /questions/46286669/how-to-retrain-logistic-regression-model-in-sklearn-with-new-data
#  but to do this we will need to pass new data into .fit(newdata, newdata)


@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment_analysis():
    """"docstring example"""
    train_model()
    if request.method == 'GET':
        text = 'happy to the point of sadness'
        print('text', text)
        if text:
            text_vector = vectorizer.transform([text])
            result = classifier.predict(text_vector)
            new_data = text + ", " + result[0] + "\n"
            with open('document.csv', 'a') as new_data_document:
                new_data_document.write(new_data)
            return (
                make_response(
                    jsonify({'sentiment': result[0], 'text': text, 'status_code': 200}), 200)
            )
        return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)
    return make_response(jsonify({'error': 'need to work out what error this should be', 'status_code': 500}), 500)


if __name__ == '__main__':
    app.run()
