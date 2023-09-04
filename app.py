from flask import Flask, render_template, request, jsonify, redirect, url_for
import joblib
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import requests
import numpy as np



app = Flask(__name__)

# Load your DataFrame 'df' here
df = pd.read_csv('time.csv')  # Replace with your actual data file

# Assuming your target column is named 'orders'
target_series = df['orders']


# Exogenous variables
exog_variables = df[['temperature', 'media_spend']]  # Adjust as needed

# Load the fitted model
fitted_model_filename = 'fitted_sarimax_model.joblib'
loaded_model = joblib.load(fitted_model_filename)

# Home page with input form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_predictions = int(request.form['num_predictions'])
        exog_values_list = []

        for i in range(num_predictions):
            temperature = float(request.form[f'temperature_{i}'])
            media_spend = float(request.form[f'media_spend_{i}'])
            exog_values_list.append([temperature, media_spend])

        exog_array = np.array(exog_values_list)

        # Make predictions using the loaded model for each set of exog values
        predictions = []
        for exog_values in exog_array:
            forecast = loaded_model.get_forecast(steps=1, exog=[exog_values])
            predicted_value = forecast.predicted_mean.tolist()[0]
            predictions.append(predicted_value)

        # Redirect to the result page with the predictions
        return redirect(url_for('result', predictions=predictions))
    else:
        return render_template('index.html', submitted=False)

# Result page to display predictions
@app.route('/result')
def result():
    predictions = request.args.getlist('predictions')
    return render_template('result.html', predictions=predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Welcome to the API!'

# @app.route('/predict', methods=['GET'])
# def predict():
#     # Your prediction logic here
#     return jsonify({'result': 'Prediction result'})

# if __name__ == '__main__':
#     app.run()