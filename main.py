import streamlit as st
pages={
    "main":[
        st.Page("siruu.py"),
        st.Page("imshi.py"),
    ],
    "algorithm":[
        
    ],
    "data":[
        
    ]
}
pg = st.navigation(pages)
pg.run()