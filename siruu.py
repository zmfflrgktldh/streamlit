import streamlit as st
st.title("⭐이시루의 마이페이지⭐")
st.header("안녕하세요! 시루입니다!")
st.write("""저는 파이썬 유저에요.
        저는 시루떡이 좋아요.""")
st.header("""시루의 신작 개발 현황""")
st.markdown(
    """
    <a href="https://playentry.org/project/66c9dece755e17ba33379442">링크 바로가기</a>
    """,
    unsafe_allow_html=True
)
st.header("나의 백준 실력은?")
#st.image("https://mazassumnida.wtf/api/v2/generate_badge?boj=zmfflrgktldh")
st.markdown(
    """
    <a href="https://solved.ac/profile/zmfflrgktldh">
        <img src="https://mazassumnida.wtf/api/v2/generate_badge?boj=zmfflrgktldh" />
    </a>
    """,
    unsafe_allow_html=True
)