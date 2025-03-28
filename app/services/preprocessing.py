import pickle
import pandas as pd
import os
import re
import gdown

# Define model URLs
MODEL_URLS = {
    "sbert_pipeline.pkl": "https://drive.google.com/uc?id=1tqdzXKAOfdR85zj6muE4eOhdPe57uC3l",
    "sentiment_analyzer.pkl": "https://drive.google.com/uc?id=1nJw6fiPjXW9cC79STVoI_GfuyRkMKLjo",
}

# Create directory for models
MODEL_DIR = "app/pickles"
os.makedirs(MODEL_DIR, exist_ok=True)

# Download models if not present
for model_name, url in MODEL_URLS.items():
    file_path = os.path.join(MODEL_DIR, model_name)
    if not os.path.exists(file_path):
        print(f"Downloading {model_name}...")
        gdown.download(url, file_path, quiet=False)
        print(f"Saved: {file_path}")

# Load models
with open(os.path.join(MODEL_DIR, "sbert_pipeline.pkl"), "rb") as f:
    sbert_model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "sentiment_analyzer.pkl"), "rb") as f:
    sentiment_analyzer = pickle.load(f)

def analyze_sentiment(comment):
    """Returns sentiment of the given comment."""
    if pd.isna(comment) or not isinstance(comment, str) or comment.strip() == "":
        return "neutral"
    return sentiment_analyzer(comment)[0]['label'].lower()
    

def preprocess_text(text):
    """Cleans and converts text to an embedding."""
    text = re.sub(r"[^A-Za-z0-9.,!?(){}[\]\"'@#&%+=<>*/-]+", " ", text)
    text = text.lower().strip()
    if len(text) == 0:
        return []
    return sbert_model.encode(text, normalize_embeddings=True).tolist()


