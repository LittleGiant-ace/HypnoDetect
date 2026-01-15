print("APP FILE STARTED")


from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load

ML_EXPLANATIONS = {
    "High": "Language style matches patterns commonly associated with misleading or influential responses.",
    "Medium": "Language contains mild persuasive or opinion-based cues.",
    "Low": "Language appears neutral and informational without persuasive patterns."
}


app = Flask(__name__)
CORS(app)

model = load("hypnodetect_model.joblib")
print("ML MODEL LOADED")

#Known factual misconceptions (prototype list) 
MISCONCEPTIONS = [
    {
        "keywords": ["fortune", "cookie", "origin"],
        "explanation": "Modern fortune cookies are widely believed to have been created by Japanese immigrants in the U.S., not in Japan itself."
    },
    {
        "keywords": ["10%", "brain"],
        "explanation": "Humans use most parts of their brain; the 10% claim is a myth."
    },
    {
        "keywords": ["gum", "7", "years", "stomach"],
        "explanation": "Swallowed gum usually passes through the digestive system within days."
    }
]

def check_factual_misconception(text: str):
    print("FACTUAL CHECK RUNNING")
    text_lc = text.lower()

    for item in MISCONCEPTIONS:
        if all(keyword in text_lc for keyword in item["keywords"]):
            return {
                "level": "High",
                "score": 80,
                "signal": {
                    "type": "factual_misconception",
                    "keywords": item["keywords"],
                    "explanation": item["explanation"]
                }
            }
    return None


def analyze_text(text):
    # Layer 1: ML Influence Risk 
    prediction = model.predict([text])[0]

    if prediction == "High":
        ml_score = 80
    elif prediction == "Medium":
        ml_score = 45
    else:
        ml_score = 10

    signals = [
    {
        "type": "ml_prediction",
        "explanation": ML_EXPLANATIONS.get(prediction, "ML-based pattern analysis applied.")
    }
    ]



    # Layer 2: Factual Misconception Risk 
    factual_result = check_factual_misconception(text)

    final_score = ml_score

    if factual_result:
        final_score = max(final_score, factual_result["score"])
        signals.append(factual_result["signal"])

    # Final Decision 
    if final_score >= 60:
        final_level = "High"
    elif final_score >= 25:
        final_level = "Medium"
    else:
        final_level = "Low"

    return {
        "score": final_score,
        "level": final_level,
        "signals": signals
    }



@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    result = analyze_text(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
