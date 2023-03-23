import streamlit as st

st.subheader('main_app.py')
code_main = '''
import streamlit as st
from PIL import Image


st.title("WEBAPP TEST")
st.caption('Streamlibで作ったテストアプリ')

st.subheader('敬慎院からの富士山')
image = Image.open('data/aka_fuji.jpg')
st.image(image, width=200)

st.subheader('七面山崩落個所')
video_file = open('data/shichimen.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
'''

st.code(code_main, language='python')


##############################################################


st.subheader('page1.py')
code1 = '''
import streamlit as st

st.subheader('main_app.py')
code_main = \'\'\'
import streamlit as st
from PIL import Image


st.title("WEBAPP TEST")
st.caption('Streamlibで作ったテストアプリ')

st.subheader('敬慎院からの富士山')
image = Image.open('data/aka_fuji.jpg')
st.image(image, width=200)

st.subheader('七面山崩落個所')
video_file = open('data/shichimen.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
\'\'\'

##############################################################


st.code_main(code_main, language='python')

st.subheader('page1.py')
code1 = \'\'\'

\'\'\'

st.code1(code1, language='python')


##############################################################


st.subheader('page2.py')
code2 = \'\'\'
import streamlit as st
from PIL import Image


st.title("WEBAPP TEST")
st.caption('Streamlibで作ったテストアプリ')

st.subheader('敬慎院からの富士山')
image = Image.open('data/aka_fuji.jpg')
st.image(image, width=200)

st.subheader('七面山崩落個所')
video_file = open('data/shichimen.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
\'\'\'

st.code2(code2, language='python')



###############################################################

st.subheader('page3.py')
code3 = \'\'\'
import streamlit as st
import pandas as pd


df = pd.read_csv('data/平均気温.csv', index_col='月')
st.subheader('平均気温')
st.line_chart(df)
st.subheader('2021年気温')
st.bar_chart(df['2021年'])


\'\'\'

st.code3(code3, language='python')
'''

st.code(code1, language='python')


##############################################################


st.subheader('page2.py')
code2 = '''
import streamlit as st
from PIL import Image


st.title("WEBAPP TEST")
st.caption('Streamlibで作ったテストアプリ')

st.subheader('敬慎院からの富士山')
image = Image.open('data/aka_fuji.jpg')
st.image(image, width=200)

st.subheader('七面山崩落個所')
video_file = open('data/shichimen.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
'''

st.code2(code2, language='python')



###############################################################

st.subheader('page3.py')
code3 = '''
import streamlit as st
import pandas as pd


df = pd.read_csv('data/平均気温.csv', index_col='月')
st.subheader('平均気温')
st.line_chart(df)
st.subheader('2021年気温')
st.bar_chart(df['2021年'])


'''

st.code3(code3, language='python')