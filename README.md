# HypnoDetect

HypnoDetect is a **hybrid AI system** designed to analyze AI-generated text and estimate the *risk of misleading, influential, or hallucinated responses*.

Rather than claiming absolute truth detection, HypnoDetect focuses on **risk-based analysis** using a multi-layer approach that combines machine learning with rule-based reasoning.

---

## Problem Statement

Modern AI systems can generate:
- Confident but incorrect answers
- Subtle misinformation
- Influential or persuasive language that appears factual

This makes it difficult for users to judge:
- *How trustworthy an AI response really is*
- *Whether the answer deserves extra verification*

HypnoDetect aims to assist users by **flagging potentially risky AI outputs**, not by replacing human judgment.

---

##  System Architecture (How It Works)

HypnoDetect uses a **multi-layer design**:

### 1 Machine Learning Layer
- Trained using data derived from the **TruthfulQA dataset**
- Learns linguistic patterns commonly found in misleading or incorrect answers
- Outputs a risk category (Low / High)

### 2 Hybrid Misconception Layer
- Uses a small curated set of known factual misconceptions
- Acts as an additional safety check
- Helps catch high-risk cases that ML alone may miss

### 3 Decision & Explanation Layer
- Combines signals from all layers
- Produces:
  - A **risk score (%)**
  - A **risk level**
  - **Explainable signals** describing why the result was flagged

>  A “High” result does **not** mean the statement is false.  
> It means the response shows patterns commonly associated with misleading or influential AI outputs.

---

##  Example Output

Hypnosis Level: 80% (High)

Detected Signals:
• [ml_prediction] Predicted by trained ML model
• [factual_misconception] Known misconception pattern detected


---

##  Tech Stack

- **Python** (Flask, scikit-learn)
- **TruthfulQA dataset**
- **Chrome Extension (HTML, CSS, JavaScript)**
- **Hybrid rule-based + ML reasoning**

---

##  Limitations (Important)

- HypnoDetect does **not** verify absolute factual truth
- It does **not** replace expert or human judgment
- High sensitivity may result in **false positives**
- Designed as a **prototype / research-oriented tool**

These limitations are intentional and documented.

---

##  Future Improvements

- Medium-risk classification layer
- Larger misconception knowledge base
- Confidence calibration
- Better UI explanations
- Cloud deployment for scalability

---

##  Final Note

HypnoDetect is an exploration into **AI safety, explainability, and risk-aware AI design**.  
The goal is not perfection, but transparency and thoughtful system design.

