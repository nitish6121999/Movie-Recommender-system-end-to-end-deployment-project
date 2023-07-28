import pandas as pd
import streamlit as st
import numpy as np
import pickle
import requests

def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data= response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
                  1:6]

    recommended_movies=[]
    recommend_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommend_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommend_poster

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

select_movie_name=st.selectbox('how would you?',movies['title'].values)

if st.button('Recommend'):
    recommended_movies,recommend_poster =recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommend_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommend_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommend_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommend_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommend_poster[4])