import pickle


def fast_response_sentiment(text):
    """load a response from the saved trained model"""
    vectorizer = pickle.load(open('./models/vectorizer.sav', 'rb'))
    classifier = pickle.load(open('./models/classifier.sav', 'rb'))
    text_vector = vectorizer.transform([text])
    result = classifier.predict(text_vector)
    print('result', result)
    return result[0]


if __name__ == '__main__':
    fast_response_sentiment("ok")
