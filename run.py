from threading import Thread

from flask import Flask, jsonify, make_response, request
from app.fast_response import fast_response
from app.svm_linear import train_model
from app.gather_data.sentiment_rating import write_to_dataset

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# dataset used: https://nlp.stanford.edu/sentiment/code.html need to reference this in paper

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment_analysis():
    """"method that outputs a response"""
    if request.method == 'GET':
        text = request.args.get('text')
        print(text)
        retrain_model = Thread(target=train_model)
        retrain_model.start()
        text = 'happy to the point of sadness'
        return fast_response(text)
    return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)


@app.route('/gather_data', methods=['GET', 'POST'])
def gather_data():
    """"method that outputs a response"""
    return write_to_dataset()


if __name__ == '__main__':
    app.run()
