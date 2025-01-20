#Artificial Intelligence generated Text Detector

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

# Download NLTK stopwords
nltk.download('stopwords')

# Load pre-trained model and tokenizer
def load_model():
    """Loads the Hugging Face model and tokenizer."""
    # Switching to the "roberta-base-openai-detector" model
    model_name = "roberta-base-openai-detector"  # Using OpenAI RoBERTa model for AI detection
    
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    return tokenizer, model


def extract_features(text):
    """Extracts linguistic features to identify formal, vague, or sophisticated tones."""
    # Convert text to lowercase and remove special characters
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # Tokenize text
    words = clean_text.split()

    # Load stopwords
    stop_words = set(stopwords.words('english'))

    # Count total words and unique words
    total_words = len(words)
    unique_words = len(set(words))

    # Count rare words (words not in stopwords and appear infrequently)
    word_counts = Counter(words)
    rare_words = [word for word, count in word_counts.items() if word not in stop_words and count == 1]
    rare_word_ratio = len(rare_words) / total_words if total_words > 0 else 0

    # Check for repetitive phrases or vague words
    vague_phrases = ["it depends", "there are many", "a lot of"]
    vague_count = sum(1 for phrase in vague_phrases if phrase in text.lower())

    # Compute complexity (average word length)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "rare_word_ratio": rare_word_ratio,
        "vague_count": vague_count,
        "avg_word_length": avg_word_length
    }


def detect_text(tokenizer, model, text):
    """Classifies input text as AI-generated or human-written with feature-based and logits adjustment."""
    # Extract features
    features = extract_features(text)

    print("Extracted features:")
    for key, value in features.items():
        print(f"  {key}: {value}")

    # Tokenize input text
    print("Tokenizing text...")
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Pass input through the model
    print("Processing text through the model...")
    with torch.no_grad():
        outputs = model(**inputs)

    # Get prediction (assuming binary classification: 0 = Human, 1 = AI-generated)
    logits = outputs.logits
    print(f"Logits: {logits}")  # Debugging logits output

    # Calculate confidence from logits
    confidence = torch.softmax(logits, dim=1)
    ai_confidence = confidence[0, 1].item()
    print(f"AI Confidence: {ai_confidence}")

    # Adjust prediction based on refined thresholds
    prediction = torch.argmax(logits, dim=1).item()

    if ai_confidence > 0.55:  # Adjusted threshold for AI signal
        prediction = 1  # Strong AI signal
    elif ai_confidence < 0.45:  # Adjusted threshold for Human signal
        prediction = 0  # Strong Human signal
    else:
        # Use features for refinement in borderline cases
        if features["rare_word_ratio"] < 0.3 and features["avg_word_length"] < 5.0:
            prediction = 0  # Bias toward Human-written
        elif features["avg_word_length"] > 6.5 or features["rare_word_ratio"] > 0.5:
            prediction = 1  # Bias toward AI-generated

    # Map prediction to label
    labels = {0: "Human-written", 1: "AI-generated"}
    return labels[prediction]


if __name__ == "__main__":
    print("Initializing the AI text detection application...")

    # Load model and tokenizer
    tokenizer, model = load_model()

    # Initialize text counter
    text_counter = 0

    while True:
        text_counter += 1
        print(f"\nText {text_counter}")

        # Example user input
        user_input = input("Enter text to classify: ")

        # Detect whether the input text is AI-generated or human-written
        result = detect_text(tokenizer, model, user_input)

        print(f"The input text is classified as: {result}")

        # Ask if the user wants to classify another text
        another = input("\nWould you like to classify another text? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            print("Exiting the application. Goodbye!")
            break
