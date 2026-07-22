# Movie Recommender System 🎬

A full-stack, Content-Based Movie Recommendation System built using Machine Learning and Python. This project is inspired by the CampusX implementation, utilizing Text Vectorization and Cosine Similarity to recommend movies, and featuring an interactive web UI that displays live movie posters.

## 🚀 Features
* **Content-Based Filtering:** Recommends 5 similar movies based on genres, keywords, cast, director, and overview tags.
* **Live Poster Fetching:** Uses the TMDB API to dynamically fetch and display movie posters in real-time.
* **Interactive UI:** Built with Streamlit for a smooth, responsive user interface.

## 🛠️ Tech Stack & Libraries
* **Development Environment:** JetBrains PyCharm
* **Language:** Python 3.x
* **Data Science:** Pandas, NumPy, Ast (Abstract Syntax Trees)
* **Machine Learning / NLP:** Scikit-learn (`CountVectorizer`, `cosine_similarity`)
* **Deployment & Frontend:** Streamlit
* **API Integration:** Requests (for TMDB API)
* **Model Serialization:** Pickle

## 📊 Dataset
This project uses the **TMDB 5000 Movie Dataset** from Kaggle.
* It requires two source files: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
* The data processing pipeline merges these files, cleans missing values, and processes string-ified JSON lists into clean tags.

## 🧠 How It Works (The Pipeline)
1. **Data Preprocessing:** Cleans and extracts `genres`, `keywords`, `cast` (top 3 actors), and `crew` (director) into lists.
2. **Tag Creation:** Merges all textual data columns into a single `tags` string for each movie.
3. **Vectorization:** Converts the text tags into 5,000-dimensional vectors using the **Bag of Words** (`CountVectorizer`) model, filtering out English stop words.
4. **Similarity Matrix:** Calculates the angle between movie vectors using **Cosine Similarity**.
5. **Model Export:** The cleaned dataframe (`movie_dict.pkl`) and the similarity matrix (`similarity.pkl`) are serialized using Pickle.
6. **Frontend App:** The Streamlit app loads these pickle files to compute top-5 recommendations instantly upon user selection.

## 💻 Getting Started

Follow these steps to set up and run this project locally in PyCharm:

### 1. Prerequisites
You need a TMDB API Key to fetch movie posters. 
1. Create a free account on [The Movie Database (TMDB)](https://themoviedb.org).
2. Navigate to your account settings > API to generate your API Key.

### 2. Clone the Project
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 3. Install Dependencies
Open your terminal in PyCharm and run:
```bash
pip install pandas scikit-learn streamlit requests
```

### 4. Run the Jupyter/Python Data Script
Ensure you run your data processing script first to generate the `.pkl` binary files:
```bash
python movie_recommender.py
```

### 5. Launch the Web App
Run the Streamlit server from your PyCharm terminal:
```bash
streamlit run app.py
```

## 🤝 Acknowledgments
* Special thanks to **CampusX (Nitish Singh)** for the brilliant educational tutorial and architectural guidance.
