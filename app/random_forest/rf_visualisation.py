import pandas as pd
import matplotlib.pyplot as plt
import pickle


def rf_create_graph():
    train_data = pickle.load(open('../models/train_data_RF.sav', 'rb'))
    classifier = pickle.load(open('../models/classifierRF.sav', 'rb'))
    feat_importances = pd.Series(classifier.feature_importances_, index=train_data.columns)
    feat_importances.nlargest(20).plot(kind='bar', figsize=(10, 10))
    print(feat_importances.nlargest(20))
    plt.title("Top 20 important features")
    plt.show()


if __name__ == '__main__':
    rf_create_graph()
