import joblib
import numpy as np

# Load the model

model = joblib.load('diabetes_detection_model.h5')

# Define the function to predict diabetes
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    scaled_input_data = scaler.transform(input_data)
    prediction = model.predict_proba(scaled_input_data)[:, 1]
    return prediction

# Define the function to print the prediction
def print_prediction(prediction):
    if prediction < 0.3:
        print("No diabetes")
    elif prediction < 0.5:
        print("There is a chance of diabetes in the future")
    elif prediction < 0.65:
        print("You have diabetes which is stage 1")
    else:
        print("You have diabetes")