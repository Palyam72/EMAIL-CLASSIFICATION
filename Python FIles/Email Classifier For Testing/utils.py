import re
import spacy
from langdetect import detect
from deep_translator import GoogleTranslator
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine
from bs4 import BeautifulSoup
import emoji

# Load spaCy model
nlp = spacy.load("en_core_web_lg")

# Initialize Presidio analyzer and anonymizer
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# ------------------- Add Custom Recognizers -------------------
# Aadhar Number (12 digits with optional spaces)
aadhar_pattern = Pattern(name="aadhar", regex=r"\b\d{4}\s\d{4}\s\d{4}\b", score=0.9)
aadhar_recognizer = PatternRecognizer(supported_entity="aadhar_num", patterns=[aadhar_pattern])
analyzer.registry.add_recognizer(aadhar_recognizer)

# CVV Number (3 digits)
cvv_pattern = Pattern(name="cvv", regex=r"\b\d{3}\b", score=0.85)
cvv_recognizer = PatternRecognizer(supported_entity="cvv_no", patterns=[cvv_pattern])
analyzer.registry.add_recognizer(cvv_recognizer)

# Expiry Date (MM/YY or MM/YYYY)
expiry_pattern = Pattern(name="expiry", regex=r"\b(0[1-9]|1[0-2])\/(\d{2}|\d{4})\b", score=0.85)
expiry_recognizer = PatternRecognizer(supported_entity="expiry_no", patterns=[expiry_pattern])
analyzer.registry.add_recognizer(expiry_recognizer)

# Credit/Debit Card Number (13 to 16 digits with optional separators)
credit_card_pattern = Pattern(name="credit_card", regex=r"\b(?:\d[ -]*?){13,16}\b", score=0.85)
credit_card_recognizer = PatternRecognizer(supported_entity="credit_debit_no", patterns=[credit_card_pattern])
analyzer.registry.add_recognizer(credit_card_recognizer)

# --------------------------------------------------------------

def detect_and_translate(text):
    """Detect language and translate to English if needed."""
    if detect(text) != "en":
        text = GoogleTranslator(source='auto', target='en').translate(text)
    return text

def mask_pii(text):
    """Detect and mask PII entities in the input text."""
    results = analyzer.analyze(text=text, entities=[], language='en')
    masked_result = anonymizer.anonymize(text, results)
    entities = [
        {
            "position": [entity.start, entity.end],
            "classification": entity.entity_type,
            "entity": text[entity.start:entity.end]
        } for entity in results
    ]
    return masked_result.text, entities

def clean_text(text):
    """Clean and preprocess the input text."""
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'[^\w\s]', '', text)
    text = emoji.demojize(text)
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
