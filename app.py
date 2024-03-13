import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = ("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
           .format(movie_id))
    data = requests.get(url)
    data = data.json()

    try:
        if 'poster_path' in data:
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            # Handle the case where 'poster_path' is not available
            return "No Poster Available"
    except Exception as e:
        # Handle potential API request errors
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "Error Fetching Poster"
    
movies = pickle.load(open('movies_list.pk1', 'rb'))
similarity = pickle.load(open('similarity.pk1', 'rb'))
movie_list = movies['Series_Title'].values
st.header('NETFLIX RECOMMENDATION ENGINE')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


def recommend(movie):
    index = movies[movies['Series_Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movie = []
    recommended_poster = []

 for i in distances[1:6]:
    movies_id = movies.iloc[i[0]]['id'] 
    poster_url = movies_data.iloc[i]['poster_url']
    response = requests.get(poster_url)
    recommended_movie.append(movies.iloc[i[0]]['title'])
    recommended_poster.append(fetch_poster(poster_url))
return recommended_movie, recommended_poster

if st.button('Show Recommendation'):
    recommended_movie, recommended_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_poster[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_poster[1])
    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_poster[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_poster[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_poster[4])