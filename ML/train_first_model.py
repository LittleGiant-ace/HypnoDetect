print("TRAINING WITH TRUTHFULQA DATA")

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump

# Load training data
df = pd.read_csv("truthfulqa_training_data.csv")

# CLEAN DATA (IMPORTANT)
df = df.dropna(subset=["text"])
df["text"] = df["text"].astype(str)

X = df["text"]
y = df["label"]


print("TOTAL SAMPLES:", len(df))
print("LABEL DISTRIBUTION:")
print(df["label"].value_counts())

# Build ML pipeline
model = Pipeline([
    ("vectorizer", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=5000
    )),
    ("classifier", LogisticRegression(
        max_iter=1000
    ))
])

print("STARTING TRAINING...")
model.fit(X, y)

# Save trained model
dump(model, "hypnodetect_model.joblib")

print("MODEL RETRAINED AND SAVED")
