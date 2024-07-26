import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
import joblib
import warnings

# Suppressing warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

data = pd.read_csv('uploads/diabetes.csv')

X = data.drop('Outcome', axis=1)
y = data['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

lgbm_clf = LGBMClassifier()
knn_clf = KNeighborsClassifier(n_neighbors=25)

voting_clf = VotingClassifier(
    estimators=[('knn', knn_clf), ('lgbm', lgbm_clf)],
    voting='soft',
    weights=[1, 1]
)

voting_clf.fit(X_scaled, y)

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    scaled_input_data = scaler.transform(input_data)
    prediction = voting_clf.predict_proba(scaled_input_data)[:, 1]  
    return prediction

def print_prediction(prediction):
    if prediction < 0.3:
        return "No diabetes"
    elif prediction < 0.5:
        return "There is a chance of diabetes in the future"
    elif prediction < 0.65:
        return "You have diabetes which is stage 1"
    else:
        return "You have diabetes"

# Save the model
joblib.dump(voting_clf, 'diabetes_detection_model.h5')
