import pickle
import os

import gdown

MODEL_URLS = {
    "hdbscan_model.pkl": "https://drive.google.com/uc?id=1AysIzvLBhdTWrA2gSlDbHT0CufdULR5M",
    "umap_reducer.pkl": "https://drive.google.com/uc?id=1AtQqopkoN5HtkFplQdOgyL3NMhM9jqxL",
}


MODEL_DIR = "app/pickles"
os.makedirs(MODEL_DIR, exist_ok=True)


for model_name, url in MODEL_URLS.items():
    file_path = os.path.join(MODEL_DIR, model_name)
    if not os.path.exists(file_path):
        print(f"Downloading {model_name}...")
        gdown.download(url, file_path, quiet=False)
        print(f"Saved: {file_path}")


with open(os.path.join(MODEL_DIR, "hdbscan_model.pkl"), "rb") as f:
    hdbscan_model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "umap_reducer.pkl"), "rb") as f:
    umap_reducer = pickle.load(f)


def cluster(embeddings):
    reduced_embeddings = umap_reducer.fit_transform(embeddings)
    print(reduced_embeddings)
    hdbscan_model.fit(reduced_embeddings)
    return hdbscan_model.labels_
