# 🌐 Multilingual Sentiment Analyzer

Multilingual text sentiment analysis using the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face 🤗  
Supports text input in multiple languages including Indonesian, English, Spanish, Japanese, and more 🌍

> Powered by 🤗 Transformers + Gradio UI

---

## 🚀 Live Demo  
👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/RyurexAI/Sentiment-Analyzer-Multilingual-ID)

---

## 🎯 Features

- 🔤 **Multilingual Input** — Supports sentiment analysis for many languages
- 🧠 **Star-based Sentiment Classification (1–5 stars)**, mapped to:
  - 1–2 stars → Negative 😠  
  - 3 stars → Neutral 😐  
  - 4–5 stars → Positive 😊  
- 💻 **Interactive Web UI** built with Gradio
- 📊 **Confidence Score** displayed in percentage

---

## 🧠 Model Used

- [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)  
  Trained to classify sentiment from 1 to 5 stars in various languages.

---

## 💻 Running Locally

Follow the steps below to run this project locally on your machine:

```bash
# 1. Clone the repository
git clone https://github.com/Ryurex/sentiment-multilingual.git
cd sentiment-multilingual

# 2. (Optional but recommended) Create and activate a virtual environment
python -m venv venv

# For Windows
.\venv\Scripts\activate

# For Linux/Mac
source venv/bin/activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
