import streamlit as st
choosed = st.radio("골라보세요",["문어","오징어","말미잘"])
st.write(f"당신은 {choosed}를 골랐습니다! 당신은 {choosed}입니다!")

code = '''print("참깨빵 위에 순쇠고기 패티 두장 치즈 피클 양상추 특별한 소스 양파까아지 빠랍빱빱빠~")'''
st.code(code)

choosed2=st.selectbox("골라보세요22",["문어","오징어","말미잘"])
st.write(f"당신은 {choosed2}를 먹었습니다!")