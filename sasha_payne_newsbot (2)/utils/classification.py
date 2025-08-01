import joblib

classifier = joblib.load("models/classifier.pkl")

def classify_news(tfidf_features):
    return classifier.predict(tfidf_features)[0]
