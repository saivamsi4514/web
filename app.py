from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
import joblib
import mysql.connector  # assuming you're using MySQL

# Initialize Flask app
app = Flask(name)

# Connect to the database
db = mysql.connector.connect(
    host='localhost',
    database='diabetes',
    user='root',
    password=''
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Load the saved model
voting_clf = joblib.load('diabetes_detection_model.h5')

# Create a scaler object
scaler = StandardScaler()
@app.route('/index', methods=['GET'])
def data():
    # Retrieve the latest values from the database
    cursor.execute("SELECT * FROM your_table_name ORDER BY id DESC LIMIT 1")
    latest_values = cursor.fetchone()

    # Extract the values from the latest row
    Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age = latest_values

    # Return the latest values as JSON
    return jsonify({
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    })

# Define a route for the prediction
@app.route('/formfill', methods=['GET'])
def predict():
    # Retrieve the latest values from the database
    cursor.execute("SELECT * FROM your_table_name ORDER BY id DESC LIMIT 1")
    latest_values = cursor.fetchone()

    # Extract the values from the latest row
    Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age = latest_values

    # Scale the input data
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    scaled_input_data = scaler.transform(input_data)

    # Make a prediction
    prediction = voting_clf.predict_proba(scaled_input_data)[:, 1]

    # Close the database connection
    cursor.close()
    db.close()

    # Print the prediction
    print("Prediction:", prediction)

    # Define the prediction message
    message = ''
    if prediction < 0.3:
        message = "No diabetes"
    elif prediction < 0.5:
        message = "There is a chance of diabetes in the future"
    elif prediction < 0.65:
        message = "You have diabetes which is stage 1"
    else:
        message = "You have diabetes"

    # Return the prediction as JSON
    return jsonify({'prediction': message})

# Run the Flask app
if name == 'main':
    app.run(debug=True)