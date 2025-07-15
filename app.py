import os
import pandas as pd
import joblib
from flask import Flask, request, render_template
import numpy as np
import random

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = joblib.load('dns_anomaly_detection_model.pkl')

# Home page route
@app.route('/')
def index():
    return render_template('index.html')  # Render your home page HTML

# File upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file and file.filename.endswith('.csv'):
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(file)

        # Clean column names (strip spaces)
        df.columns = df.columns.str.strip()

        # Handle missing or infinite values by replacing infinities with NaN and dropping rows with NaN values
        df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
        df.dropna(inplace=True)

        # Create a binary 'Label_Bot' column: 1 for 'Bot' and 0 for others
        df['Label_Bot'] = df['Label'].apply(lambda x: 1 if x == 'Bot' else 0)

        # Extract features (all columns except 'Label' and 'Label_Bot')
        X = df.drop(columns=['Label', 'Label_Bot'])

        # Randomly select 20 rows from the dataset for prediction
        random_samples = X.sample(n=20, random_state=42)

        # Get prediction probabilities instead of just predicting the class
        prediction_probs = model.predict_proba(random_samples)

        # Get the class with the highest probability (0 for Normal, 1 for Anomaly)
        predictions = np.argmax(prediction_probs, axis=1)

        # Convert probabilities and predictions into readable format
        predictions = ['Normal' if pred == 1 else 'Anomaly' for pred in predictions]

        # Combine the random samples, probabilities, and predictions into a DataFrame
        result_df = random_samples.copy()
        result_df['Prediction'] = predictions
        result_df['Anomaly Probability'] = prediction_probs[:, 1]  # Probability of being "Anomaly"

        # Convert result to HTML table format for rendering
        result_html = result_df.to_html(classes='table table-bordered', index=False)

        return render_template('upload_result.html', result=result_html)  # Render result page with table
    else:
        return "Invalid file type. Please upload a CSV file."

if __name__ == '__main__':
    app.run(debug=True)
