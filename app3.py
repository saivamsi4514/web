from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
import joblib
import mysql.connector

app = Flask(__name__)

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
def load_model():
    return joblib.load('diabetes_detection_model.h5')

# Create a scaler object
scaler = StandardScaler()

@app.route('/save_model')
def save_model():
    # Your code to save the model
    import numpy as np 
    import pandas as pd 
    from sklearn.preprocessing import StandardScaler 
    from lightgbm import LGBMClassifier
    from sklearn.neighbors import KNeighborsClassifier 
    from sklearn.ensemble import VotingClassifier
    import joblib

    data = pd.read_csv('uploads/diabetes.csv')

    X = data.drop('Outcome', axis=1) 
    y = data['Outcome']

    scaler = StandardScaler() 
    
    X_scaled = scaler.fit_transform(X)

    lgbm_clf = LGBMClassifier() 
    knn_clf = KNeighborsClassifier(n_neighbors=25)

    voting_clf = VotingClassifier( estimators=[('knn', knn_clf), ('lgbm', lgbm_clf)], voting='soft', weights=[1, 1] )

    voting_clf.fit(X_scaled, y)
    return joblib.dump(voting_clf, 'diabetes_detection_model.h5')

@app.route('/load_model')
def load_model_route():
    model = load_model()
    return 'Model loaded successfully!'

@app.route('/index', methods=['GET'])
def index():
    cursor.execute("SELECT * FROM parameters_table ORDER BY age DESC LIMIT 1")
    latest_values = cursor.fetchone()
    if latest_values:
        Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age = latest_values
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
    else:
        return 'No data available'

@app.route('/formfill', methods=['GET','POST'])
def formfill():
    model = load_model()
    cursor.execute("SELECT * FROM parameters_table ORDER BY age DESC LIMIT 1")
    latest_values = cursor.fetchone()
    if latest_values:
        Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age = latest_values
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        scaled_input_data = scaler.transform(input_data)
        prediction = model.predict_proba(scaled_input_data)[:, 1]
        cursor.close()
        db.close()
        message = ''
        if prediction < 0.3:
            message = "No diabetes"
        elif prediction < 0.5:
            message = "There is a chance of diabetes in the future"
        elif prediction < 0.65:
            message = "You have diabetes which is stage 1"
        else:
            message = "You have diabetes"
        return jsonify({'prediction': message})
    else:
        return 'No data available'

if __name__ == '__main__':
    app.run(debug=True)
