from flask import Flask, render_template, request
from model import predict_diabetes, print_prediction
import joblib
from app7 import visualization_blueprint

app = Flask(__name__)

# Load the model
model = joblib.load('diabetes_detection_model.h5')

# Register the blueprint
app.register_blueprint(visualization_blueprint, url_prefix='/visualization')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        glucose = int(request.form['glucose'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        blood_pressure = int(request.form['blood_pressure'])
        pregnancies = int(request.form['pregnancies'])
        dpf = float(request.form['dpf'])
        skin_thickness = int(request.form['skin_thickness'])

        # Predict using the model
        prediction = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)

        # Print and format prediction
        prediction_text = print_prediction(prediction)

        return render_template('result.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
