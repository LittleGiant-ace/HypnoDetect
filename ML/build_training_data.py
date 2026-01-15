from datasets import load_dataset
import pandas as pd

print("LOADING TRUTHFULQA...")
dataset = load_dataset("truthful_qa", "generation")
print("DATASET LOADED")

texts = []
labels = []

for item in dataset["validation"]:

    # Low Risk: best answer
    if item["best_answer"]:
        texts.append(item["best_answer"])
        labels.append("Low")

    # Low Risk: all correct answers
    for ans in item["correct_answers"]:
        texts.append(ans)
        labels.append("Low")

    # High Risk: all incorrect answers
    for ans in item["incorrect_answers"]:
        texts.append(ans)
        labels.append("High")

df = pd.DataFrame({
    "text": texts,
    "label": labels
})

print("TOTAL TRAINING SAMPLES:", len(df))
print("\nSAMPLE ROWS:")
print(df.head())

df.to_csv("truthfulqa_training_data.csv", index=False)
print("\nTRAINING DATA SAVED AS truthfulqa_training_data.csv")
