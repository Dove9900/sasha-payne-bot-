import spacy
import joblib

nlp = spacy.load("en_core_web_sm")
tfidf_vectorizer = joblib.load("models/tfidf.pkl")

def get_tfidf_features(text):
    return tfidf_vectorizer.transform([text])

def get_pos_tags(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def get_dependencies(text):
    doc = nlp(text)
    return [(token.text, token.dep_, token.head.text) for token in doc]
