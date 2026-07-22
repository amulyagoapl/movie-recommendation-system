# # import streamlit as st
# # import pickle
# # import pandas as pd
# #
# #
# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
# #
# #     recommended_movies = []
# #     for i in movies_list:
# #         recommended_movies.append((movie.iloc[i[0]].title))
# #     return  recommended_movies
# #
# # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # movies =  pd.DataFrame(movies_dict)
# # similarity = pickle.load(open('similarity.pkl','rb'))
# #
# # st.title("Movie Recommender System")
# #
# #
# # option = st.selectbox('Select a movie:', movies['title'].values)
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500" + data['poster_path']
#
#
#
# def recommend(movie_name):
#     # Find the index of the selected movie
#     movie_index = movies[movies['title'] == movie_name].index[0]
#     distances = similarity[movie_index]
#
#     # Fetch top 5 similar movies
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_poster = []
#     for i in movies_list:
#         # BUG FIX: Changed 'movie' to 'movies' to reference the DataFrame
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_poster.append(fetch_poster(i[0]))
#     return recommended_movies,recommended_movies_poster
#
#
# # Load data assets safely
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Build Streamlit UI
# st.title("Movie Recommender System")
#
# option = st.selectbox('Select a movie:', movies['title'].values)
#
#
#
#
# # Trigger recommendations on button click
# if st.button('Recommend'):
#     names,posters = recommend(option)
#     col1, col2, col3, col4, col5 = st.beta_colums(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])
#
#
#
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    # Safe API call using the actual TMDB ID
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        # Fallback if the movie does not have a poster path
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        return "https://placeholder.com"
    except Exception:
        return "https://placeholder.com"


def recommend(movie_name):
    # Find index of the movie
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]

    # Fetch top 5 similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        # FIXED: Extracting the actual unique movie ID from your dataframe
        actual_movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # FIXED: Passing the actual_movie_id to the API instead of the index loop tracker
        recommended_movies_poster.append(fetch_poster(actual_movie_id))

    return recommended_movies, recommended_movies_poster


# Load data assets safely
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Build Streamlit UI
st.title("Movie Recommender System")

option = st.selectbox('Select a movie:', movies['title'].values)

# Trigger recommendations on button click
if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(option)

        # FIXED: Corrected spelling and removed deprecated 'beta_' prefix
        columns = st.columns(5)

        # Cleaned up layout using a short loop instead of copying repetitive blocks
        for index in range(5):
            with columns[index]:
                st.text(names[index])
                st.image(posters[index])

