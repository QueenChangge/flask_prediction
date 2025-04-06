from flask import Flask, render_template, request
import joblib
# from sklearn.cluster import KMeans
# from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.metrics.pairwise import rbf_kernel
import pandas as pd
# from model.utils import column_ratio

app = Flask(__name__)
model = joblib.load('model/my_california_housing_model.pkl')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/house-price-prediction", methods=['GET', 'POST'])
def form_prediction():
    if request.method == 'GET':
        return render_template('form_prediction.html')
        
    elif request.method == 'POST':
        # Extracting form data
        data = {
            'longitude': [float(request.form['longitude'])],
            'latitude': [float(request.form['latitude'])],
            'housing_median_age': [float(request.form['housing_median_age'])],
            'total_bedrooms': [float(request.form['total_bedrooms'])],
            'total_rooms': [float(request.form['total_rooms'])],
            'population': [float(request.form['population'])],
            'households': [float(request.form['households'])],
            'median_income': [float(request.form['median_income'])],
            'ocean_proximity': [request.form['ocean_proximity']]  # Keep as string for categorical data
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(data)

        # Debugging: Print the DataFrame (optional)
        print(input_df)

        # Make prediction
        prediction = model.predict(input_df)
        return render_template('output_prediction.html', data=prediction)
        
        
        

# @app.route("/house-price-prediction", )
# def form_prediction():
#     return render_template('form_prediction.html')

if __name__ == '__main__':
	app.run(debug=True)