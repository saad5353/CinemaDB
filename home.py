import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os
import requests

st.set_page_config(page_title='CinemaDB', page_icon=':movie_camera:')
st.header('CinemaDB 🎬')
st.subheader('See trending movies and tv shows')
st.write('This is a simple web app that lets you see trending movies and tv shows. 🤖')
load_dotenv()
api_key = os.getenv('API_KEY')


selected2 = option_menu(None, ["Movies", "TV Shows"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Movies":
    with st.spinner('🔍 Searching for trending movies...'):
        api_url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}'
        response = requests.get(api_url)
        data = response.json()
        
