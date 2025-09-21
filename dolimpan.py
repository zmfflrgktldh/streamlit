import streamlit as st
import random
배웠던거=['code','radio','image','selectbox','multiselect','button']
뽑을거=st.multiselect("쓰고싶은거 골라봐요",배웠던거,default=배웠던거)
def 뽑기():
    try:
        st.write(*random.sample(뽑을거,3))
    except:
        st.write("3개 이상 골라요")

if st.button("뽑기"):
    뽑기()