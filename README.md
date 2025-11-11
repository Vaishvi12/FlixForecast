# FlixForecast 
## Movie Success Prediction

## Overview

**FlixForecast** is a data-driven project designed to predict the success of movies using IMDb ratings and other key factors that influence movie success. The project uses machine learning algorithms to analyze historical movie data, providing filmmakers, producers, and stakeholders with actionable insights into audience preferences, genre trends, and other factors contributing to a movie's performance.

By forecasting IMDb ratings and analyzing genre trends, **FlixForecast** helps optimize decision-making in the film industry, assisting in areas like production, marketing, and resource allocation.

## Problem Statement

The film industry often struggles with predicting which movies will succeed or fail. Multiple factors, including genre, director, cast, and production budget, affect a movie's reception and box office performance. Unfortunately, filmmakers and stakeholders lack reliable tools to forecast audience reactions and optimize movie strategies.

**FlixForecast** seeks to solve this problem by using machine learning to predict IMDb ratings and analyze data patterns. This tool aims to help industry professionals make more informed decisions by providing insights into the factors that influence movie success.

## Key Features

- **Predictive Model:** Uses IMDb data to predict the potential success of a movie based on various factors like genre, director, cast, and more.
- **Genre Trend Analysis:** Provides visualizations to explore how different genres perform over time and what factors influence their popularity.
- **Interactive Web Interface:** A user-friendly platform where users can input movie details to get predictions and view interactive visualizations.
- **Backend Integration:** Uses Flask and MongoDB for dynamic data interaction, making predictions and visualizations accessible in real-time.

## Project Workflow

### 1. Data Collection

**Objective:** Gather a comprehensive dataset of movie information from IMDb.

- **Tools Used:** Python, Octoparse
- **Dataset:** 5 years of movie data with approximately 10,000 entries per year.
- **Data Columns:** Year, Certificate, Runtime, Score, Director, Cast, Number of Votes, Gross Revenue, Genre, IMDb Rating, Movie Title, etc.

### 2. Data Cleaning & Model Development

**Objective:** Clean and preprocess the collected data, then develop a machine learning model for prediction.

#### Data Preprocessing:

- Remove irrelevant or redundant columns.
- Handle missing values (using mean imputation for rating columns).
- Focus on key features like 'genre,' 'rating,' and 'gross revenue' for model training.

#### Predictive Model:

- A **RandomForest Regressor** model is trained to predict IMDb ratings based on historical movie data.

### 3. Frontend Development

**Objective:** Create an interactive and visually appealing web interface.

#### Technologies:

- **HTML** for structuring the webpage.
- **CSS** for styling the web page and ensuring a clean, modern design.
- **JavaScript** for dynamic functionality, such as dropdowns for genre selection.
- **DOM Manipulation** for updating content based on user input.
- `<marquee>` tag for creating a smooth scrolling effect.

### 4. Data Visualizations

**Objective:** Generate insightful visualizations to explore genre trends, audience preferences, and movie performance.

#### Visualization Tools:

- **Jupyter Notebook** is used for generating bar charts, pie charts, and other visual representations.
- Insights into genre popularity, rating distribution, and historical box office performance are visualized.

#### Flask Backend:

- The Flask server provides a backend to interact with the machine learning model and serve predictions and visualizations dynamically.

### 5. Backend Integration

**Objective:** Store the data efficiently and serve the predictions and visualizations through the web interface.

- **Database:** MongoDB is used for storing the movie data.
  - The data is stored in **JSON** and **Excel** formats for flexibility.
  - MongoDB enables fast data retrieval and ensures scalability as the project grows.

#### Flask Framework:

- The backend logic is implemented using Flask, which serves the model predictions and visualizations to the user interface.
- AJAX requests from the frontend dynamically fetch the predictions and visualizations.

## Technologies Used

- **Data Collection & Analysis:** Python, Octoparse, Pandas, NumPy
- **Machine Learning:** RandomForest Regressor (Scikit-learn)
- **Web Development:** HTML, CSS, JavaScript
- **Backend:** Flask, MongoDB, pymongo
- **Data Visualization:** Jupyter Notebook, Matplotlib, Seaborn

## Installation and Setup

### Prerequisites

- Python 3.x
- MongoDB (either local or cloud instance)
- Flask
- Required Python libraries (listed below)

### Steps to Set Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FlixForecast.git
   cd FlixForecast
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**

   * Make sure MongoDB is installed and running on your local machine or cloud.
   * Update the MongoDB connection details in `config.py` if necessary.

4. **Run the Flask Application:**

   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://localhost:5000` to explore the web application.

### Dependencies

* Flask
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* pymongo
* Requests

## Usage

1. **Explore Genre Trends:**

   * Use the interactive visualizations to see how different genres perform over time.
   * Filter the data by year, genre, or movie rating to find patterns.

2. **Predict IMDb Ratings:**

   * Enter a movie's details (e.g., genre, director, cast) and receive a prediction for its IMDb rating.
   * Compare predicted ratings with actual ratings of similar movies.

3. **Interactive Charts:**

   * View dynamic charts and graphs showing box office trends, rating distributions, and genre performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
