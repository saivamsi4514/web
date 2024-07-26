import os
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from flask import Blueprint, render_template

visualization_blueprint = Blueprint('visualization', __name__, template_folder='templates')

# Load data from CSV file
data = pd.read_csv('uploads/diabetes.csv')

# Ensure the directory 'static/images' exists
images_dir = os.path.join('static', 'images')
os.makedirs(images_dir, exist_ok=True)

@visualization_blueprint.route('/visualization')
def visualization():
    # Generate plots
    bar_chart = generate_bar_chart()
    pie_chart = generate_pie_chart()
    histogram = generate_histogram()
    box_plot = generate_box_plot()
    scatter_plot = generate_scatter_plot()
    dist_plot = generate_dist_plot()

    return render_template('index2.html', 
                           bar_chart=bar_chart,
                           pie_chart=pie_chart,
                           histogram=histogram,
                           box_plot=box_plot,
                           scatter_plot=scatter_plot,
                           dist_plot=dist_plot)

def generate_bar_chart():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='SkinThickness', hue='Outcome', data=data.head(200), palette='coolwarm')
    plt.xlabel('Skin Thickness')
    plt.ylabel('Count')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'bar_chart.png'), format='png')
    buffer.seek(0)
    bar_chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return bar_chart

def generate_pie_chart():
    filtered_data = data.head(50)

    # Aggregate the data to get counts of each unique value in the pregnancies attribute
    pregnancies_counts = filtered_data['Pregnancies'].value_counts()

    # Define labels and sizes for the pie chart
    labels = pregnancies_counts.index
    sizes = pregnancies_counts.values

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.ylabel('no.of pregnancies')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'pie_chart.png'), format='png')
    buffer.seek(0)
    pie_chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return pie_chart

def generate_histogram():
    plt.figure(figsize=(10, 6))
    sns.histplot(data['BloodPressure'], bins=20,  color='red',edgecolor='black',kde=True)
    #plt.hist(data['BloodPressure'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('BP')
    plt.ylabel('Frequency')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'histogram.png'), format='png')
    buffer.seek(0)
    histogram = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return histogram

def generate_box_plot():
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Age', y='BloodPressure', data=data.head(100))

    # Add labels and title
    plt.xlabel('Age')
    plt.ylabel('Blood Pressure (bp)')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'box_plot.png'), format='png')
    buffer.seek(0)
    box_plot = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return box_plot

def generate_scatter_plot():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='BMI', y='SkinThickness', data=data, hue='Outcome', palette='coolwarm')
    plt.axhline(y=28, color='r', linestyle='--', label='skinthickness=28')
    plt.axvline(x=28, color='b', linestyle='--', label='BMI=28')
    plt.xlabel('BMI')
    plt.ylabel('Skin Thickness')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'scatter_plot.png'), format='png')
    buffer.seek(0)
    scatter_plot = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return scatter_plot



def generate_dist_plot():
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data[data['Outcome'] == 1]['Glucose'], shade=True, color='red', label='Diabetic')
    sns.kdeplot(data[data['Outcome'] == 0]['Glucose'], shade=True, color='blue', label='Non-Diabetic')
    plt.xlabel('Glucose Level')
    plt.ylabel('Density')
    buffer = io.BytesIO()
    plt.savefig(os.path.join(images_dir, 'dist_plot.png'), format='png')
    buffer.seek(0)
    line_chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return line_chart


# Remaining visualization functions...

if __name__ == '__main__':
    app.run(debug=True,port=5001)
