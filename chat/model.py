from sentence_transformers import SentenceTransformer
import os

# Path to store the model locally after first download
MODEL_PATH = './models/S-BioBert'

# Check if model exists at the given path
def load_model():
    model = None

    # Check if model exists locally
    if os.path.exists(MODEL_PATH):
        print(f"Loading model from local path: {MODEL_PATH}")
        try:
            # Try to load the model from the local directory
            model = SentenceTransformer(MODEL_PATH)
            print("Model loaded successfully from local path.")
        except Exception as e:
            print(f"Error loading local model: {e}")
            model = None

    # If model doesn't exist locally, attempt to download it
    if model is None:
        print("Model not found locally. Downloading from Hugging Face...")
        try:
            # Download and load the model from Hugging Face
            model = SentenceTransformer('pritamdeka/S-BioBert-snli-multinli-stsb')
            # Save the model locally for future use
            model.save(MODEL_PATH)
            print(f"Model downloaded and saved to {MODEL_PATH}")
        except Exception as e:
            print(f"Error downloading model from Hugging Face: {e}")
            model = None

    # Ensure model is successfully loaded
    if model is None:
        raise RuntimeError("Failed to load or download the model.")

    return model

# Load model when the script is executed
model = load_model()
