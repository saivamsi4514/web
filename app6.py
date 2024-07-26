from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from CSV file
    df = pd.read_csv('uploads/diabetes.csv')
    
    # Generate plots
    bar_chart = generate_bar_chart(df)
    pie_chart = generate_pie_chart(df)
    histogram = generate_histogram(df)
    box_plot = generate_box_plot(df)
    scatter_plot = generate_scatter_plot(df)
   
    
    return render_template('index.html', 
                           bar_chart=bar_chart,
                           pie_chart=pie_chart,
                           histogram=histogram,
                           box_plot=box_plot,
                           scatter_plot=scatter_plot,
                           )

def generate_bar_chart(df):
    # Group data and calculate sum
    data = df.groupby('BloodPressure')['Age'].sum()
    
    # Plot bar chart
    plt.figure(figsize=(8, 6))
    data.plot(kind='bar')
    plt.title('Bar Chart')
    plt.xlabel('age')
    plt.ylabel('blood_pressure')
    
    # Save plot to buffer and encode as base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    bar_chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return bar_chart

def generate_pie_chart(df):
    # Group data and calculate sum
    data = df.groupby('Age')['Glucose'].sum()
    
    # Plot pie chart
    plt.figure(figsize=(8, 6))
    data.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.ylabel('age')
    
    # Save plot to buffer and encode as base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    pie_chart = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return pie_chart

def generate_histogram(df):
    # Plot histogram
    plt.figure(figsize=(8, 6))
    df['BMI'].plot(kind='hist', bins=10)
    plt.title('Histogram')
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    
    # Save plot to buffer and encode as base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    histogram = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return histogram

def generate_box_plot(df):
    # Plot box plot
    plt.figure(figsize=(8, 6))
    df.boxplot(column='Insulin', by='BloodPressure')
    plt.title('Box Plot')
    plt.xlabel('insulin')
    plt.ylabel('blood_pressure')
    
    # Save plot to buffer and encode as base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    box_plot = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return box_plot

def generate_scatter_plot(df):
    # Plot scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df['BMI'], df['SkinThickness'])
    plt.title('Scatter Plot')
    plt.xlabel('BMI')
    plt.ylabel('skinthickness')
    
    # Save plot to buffer and encode as base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    scatter_plot = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return scatter_plot


if __name__ == '__main__':
    app.run(debug=True)
