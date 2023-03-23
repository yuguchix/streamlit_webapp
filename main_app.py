import streamlit as st
from PIL import Image


st.title("WEBAPP TEST")
st.caption('こちらはStreamlibで作ったテストアプリです。')

image = Image.open('data/aka_fuji.jpg')
st.image(image, width=200)

video_file = open('data/shichimen.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)