import pickle
from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd

app= Flask(__name__)
# Load the model
model = pickle.load(open('calorie_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/predict_api', methods=['POST'])
def predict_api():
    if request.method == 'POST':
        # Get form data
        gender = request.form['gender'] 
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])
        heart_rate = float(request.form['heart_rate'])
        body_temp = float(request.form['body_temp'])
         
        # Convert gender to numeric value
        gender = 0 if gender.lower() == 'male' else 1




        # Prepare input for model (reshape as needed)
        input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(input_data)
        calories_burnt = prediction[0]

        # Render result page or return JSON
        return render_template('result.html', calories=calories_burnt)

if __name__ == "__main__":
    app.run(debug=True)

        