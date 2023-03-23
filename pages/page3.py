import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib as plt



df = pd.read_csv('data/平均気温.csv', index_col='月')
# st.dataframe(df)
# st.table(df)
st.subheader('平均気温')
st.line_chart(df)
st.subheader('2021年気温')
st.bar_chart(df['2021年'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021年'])
ax.set_title('matplotlib graph')
st.pyplot(fig)
