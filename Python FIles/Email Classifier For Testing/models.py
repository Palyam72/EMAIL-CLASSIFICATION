import pickle
import numpy as np

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model1.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler=pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def predict_category(text):
    vector = vectorizer.transform([text])
    vector=scaler.transform(vector)
    prediction = model.predict(vector)  # e.g. [0.]
    prediction = np.array(prediction).reshape(-1, 1)  # <- convert to 2D
    label = encoder.inverse_transform(prediction)[0][0]  # get first row, first col
    return label
