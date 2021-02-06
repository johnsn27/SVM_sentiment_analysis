from threading import Thread

from flask import Flask, jsonify, make_response, request
from svm_linear import train_model
from fast_response import fast_response
from gather_data.new_articles import read_csv

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment_analysis():
    """"method that outputs a response"""
    if request.method == 'GET':
        retrain_model = Thread(target=train_model)
        retrain_model.start()
        text = 'happy to the point of sadness'
        return fast_response(text)
    return make_response(jsonify({'error': 'sorry! unable to parse', 'status_code': 500}), 500)


@app.route('/gather_data', methods=['GET', 'POST'])
def gather_data():
    """"method that outputs a response"""
    read_csv()


if __name__ == '__main__':
    app.run()