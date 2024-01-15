import streamlit as st
import pickle
import pandas as pd

def recommend(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        movie_id = i[0]
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

#st.image('C:\\Users\\DELL\\Downloads\\Image theatre.jpg')

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name, movies, similarity)
    for i in recommendations:
        st.write(i)
