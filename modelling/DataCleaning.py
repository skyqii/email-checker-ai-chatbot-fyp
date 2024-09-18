import re
import nltk
from nltk.corpus import stopwords
from transformers import GPT2Tokenizer

# Download required resources from nltk
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Initialize GPT-2 tokenizer from Hugging Face
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# List of stopwords from NLTK
STOPWORDS = set(stopwords.words('english'))

# Define the cleaning pipeline

def remove_special_characters(text):
    """Remove special characters, keeping only alphanumeric and basic punctuation."""
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, ' ', text)

def lowercase_text(text):
    """Convert all characters in the text to lowercase."""
    return text.lower()

def remove_extra_whitespace(text):
    """Remove extra whitespaces, tabs, and newlines."""
    return re.sub(r'\s+', ' ', text).strip()

def remove_stopwords(text):
    """Remove stopwords from text"""
    tokens = tokenizer.tokenize(text)  # Tokenize using GPT-2 tokenizer
    # filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(tokens)


def clean_text_pipeline(text):
    text = remove_special_characters(text)
    text = lowercase_text(text)
    text = remove_extra_whitespace(text)
    return text

# Sample usage: reading from a file
with open(r'data/all_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = clean_text_pipeline(text)
print(cleaned_text)
