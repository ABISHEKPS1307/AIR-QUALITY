from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('city_day.csv')
data['Date'] = pd.to_datetime(data['Date'])  # Convert to datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    city = None

    if request.method == 'POST':
        city = request.form['city']
        # Filter data for the specified city
        result = data[data['City'].str.lower() == city.lower()]  # Case insensitive match

    return render_template('index.html', result=result, city=city)

if __name__ == '__main__':
    app.run(debug=True)
