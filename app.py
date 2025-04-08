from transformers import pipeline
import gradio as gr

# Ganti model ke yang multilingual dan compatible!
model_id = "nlptown/bert-base-multilingual-uncased-sentiment"

# Load pipeline
sentiment_model = pipeline("sentiment-analysis", model=model_id)

# Mapping fungsi bintang ke label sentimen
def map_label(star_label):
    star = int(star_label.split()[0])  # Ambil angka dari "5 stars", dst
    if star <= 2:
        return "Negative 😠"
    elif star == 3:
        return "Neutral 😐"
    else:
        return "Positive 😊"

# Fungsi prediksi
def predict_sentiment(text):
    result = sentiment_model(text)[0]
    label = map_label(result['label'])
    confidence = round(result['score'] * 100, 2)
    return f"Sentiment: {label}\nConfidence: {confidence}%"

# Gradio UI
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Tulis pendapatmu di sini..."),
    outputs="text",
    title="🌐 Multilingual Sentiment Analyzer",
    description="Analisis sentimen teks dalam berbagai bahasa menggunakan model multilingual BERT."
)

iface.launch()
