# app.py
import pickle

# Load the preprocessor and model once
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_rent(user_input_dict):
    import pandas as pd

    # Create input DataFrame
    input_df = pd.DataFrame([user_input_dict])

    # Preprocess input
    processed_input = preprocessor.transform(input_df)

    # Predict
    predicted_rent = model.predict(processed_input)[0]
    return int(predicted_rent)
