from datasets import load_dataset

print("LOADING TRUTHFULQA...")

dataset = load_dataset("truthful_qa", "generation")

print("DATASET LOADED")
print(dataset)
