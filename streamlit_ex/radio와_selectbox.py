import streamlit as st
st.header("radio와 selectbox")
choosed = st.radio("골라보세요",["문어","오징어","말미잘"])
st.write(f"당신은 {choosed}를 골랐습니다! 당신은 {choosed}입니다!")

choosed2=st.selectbox("골라보세요22",["문어","오징어","말미잘"])
st.write(f"당신은 {choosed2}를 먹었습니다!")