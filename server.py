from flask import Flask, render_template, request, redirect, url_for,send_file
from joblib import dump, load 
import json
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.model_selection import train_test_split

loaded_model = load("model.pkl")
loaded_encoder = load("encoder.pkl")

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/analysis')
def blockbuster():
    return render_template('analysis.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/result', methods=['POST'])
def result():
    selected_option = request.form.get('genre')
    with open('output.json', 'r') as f:
        fixed_outputs = json.load(f)

    # Get the fixed output for the selected genre
    prediction = fixed_outputs.get(selected_option, "Not available")

    return render_template('result.html', option=prediction)




@app.route('/<selected_year>')
def genre_pie_chart(selected_year):
    # Load data for the selected year
    return send_file(f'static/genre_pie_chart_{selected_year}.png', mimetype='image/png')
    csv_file = f"C:\\Users\malay\\OneDrive\\Desktop\\Ma-Sa-La\\Imdb_Prediction\\dataset\\Ma-Sa-La.{selected_year}.csv"
    data = pd.read_csv(csv_file)

    # Extract and clean genres
    all_genres = pd.concat([data['genre'].str.strip(), data['genre1'].str.strip(), data['genre2'].str.strip()])
    genre_counts_combined = all_genres.value_counts()

    # Generate the pie chart
    plt.figure(figsize=(10, 8))
    genre_counts_combined.head(10).plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Genre Distribution - Top 10 - {selected_year}')
    plt.ylabel('')

    # Save the pie chart to a file
    plt.savefig(f'static/genre_pie_chart_{selected_year}.png')
    plt.close()

    # Send the file in the response




if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()