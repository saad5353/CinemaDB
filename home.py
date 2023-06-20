import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os
import requests

st.set_page_config(page_title='CinemaDB', page_icon=':movie_camera:', layout='wide')
st.header('CinemaDB 🎬')
st.subheader('See trending movies and tv shows')
st.write('This is a simple web app that lets you see trending movies and tv shows. 🤖')
load_dotenv()
api_key = os.getenv('API_KEY')


selected2 = option_menu(None, ["Trending Movies", "Trending TV Shows", "Search"],
    icons=["tv", "tv", "search"],
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Trending Movies":
    with st.spinner('🔍 Searching for trending movies...'):
        api_url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}'
        response = requests.get(api_url)
        if response.status_code != 200:
            st.error('Error loading data')
        data = response.json()
        # parse results
        for movie in data['results']:
            st.divider()
            c = st.container()
            with c:
                c1, c2 = st.columns((3,6), gap="small")
                with c1:
                    st.header(f"{movie['title']}")
                    st.image(f"https://image.tmdb.org/t/p/w300/{movie['poster_path']}")
                with c2:
                    st.success(f"**Overview:** {movie['overview']}", icon="📝")
                    st.error(f"**Release Date:** {movie['release_date']}", icon="📅")
                    st.error(f"**Popularity:** {movie['popularity']}", icon="🔥")
                    st.error(f"**Vote Average:** {movie['vote_average']}", icon="⭐")
                    st.error(f"**Original Language:** {movie['original_language']}", icon="🌐")
                    if movie['adult'] == False:
                        st.error(f"**Adult Rated:** No", icon="🔞")
                    else:
                        st.error(f"**Adult Rated:** Yes", icon="🔞")
            st.divider()
                

elif selected2 == "Trending TV Shows":
    with st.spinner('🔍 Searching for trending tv shows...'):
        api_url = f'https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}'
        response = requests.get(api_url)
        if response.status_code != 200:
            st.error('Error loading data')
        data = response.json()
        # parse results
        for tv in data['results']:
            c = st.container()
            with c:
                c1, c2 = st.columns((3,6), gap="small")
                with c1:
                    st.header(f"{tv['name']}")
                    st.image(f"https://image.tmdb.org/t/p/w300/{tv['poster_path']}")
                with c2:
                    st.success(f"**Overview:** {tv['overview']}", icon="📝")
                    st.error(f"**Release Date:** {tv['first_air_date']}", icon="📅")
                    st.error(f"**Popularity:** {tv['popularity']}", icon="🔥")
                    st.error(f"**Vote Average:** {tv['vote_average']}", icon="⭐")
                    st.error(f"**Original Language:** {tv['original_language']}", icon="🌐")
                    if tv['adult'] == False:
                        st.error(f"**Adult Rated:** No", icon="🔞")
                    else:
                        st.error(f"**Adult Rated:** Yes", icon="🔞")
            st.divider()
        
