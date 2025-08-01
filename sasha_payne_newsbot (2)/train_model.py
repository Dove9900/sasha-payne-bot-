import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# ✅ Make sure the models folder exists
os.makedirs("models", exist_ok=True)

# Load sample data
df = pd.read_csv("data/sample_news.csv")
X = df["text"]
y = df["category"]

# Create a pipeline with TF-IDF and Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=1000)),
    ("clf", LogisticRegression(max_iter=500))
])

# Fit the model
pipeline.fit(X, y)

# Save TF-IDF and Classifier models
joblib.dump(pipeline.named_steps["tfidf"], "models/tfidf.pkl")
joblib.dump(pipeline.named_steps["clf"], "models/classifier.pkl")

print("✅ Models saved in the 'models' directory.")