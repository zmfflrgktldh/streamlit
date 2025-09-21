import streamlit as st
import os
pages = {}
topics = [
    "mypage",
    "algorithm",
    "DataScience",
    "streamlit_ex",
    "실습",
]
for topic in topics:
    pages[topic]=[]

    for file in os.listdir(topic):
        page=st.Page(f'{topic}/{file}',title=file[0:-3].replace("_"," "))
        pages[topic].append(page)

pg = st.navigation(pages)
pg.run()