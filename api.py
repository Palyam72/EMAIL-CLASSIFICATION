from models import predict_category
from utils import detect_and_translate, mask_pii, clean_text

def classify_email(email_text):
    translated = detect_and_translate(email_text)
    masked_email, entities = mask_pii(translated)
    cleaned = clean_text(masked_email)
    category = predict_category(cleaned)
    return {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }