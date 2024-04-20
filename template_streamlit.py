import streamlit as st

st.set_page_config(layout="wide")
st.title("title")

st.divider()

with st.sidebar:
    st.image("default.png")
    st.slider("id12341234")
    st.slider("id1325653")
    st.slider("id346746789")

with st.container() as cont:
    col1, col2 = st.columns([380,113])
    with col1:
        with st.container():
            col3,col4,col5 = st.columns([120,120,120])
            with col3:
                st.image("default.png")
            with col4:
                st.image("default.png")
            with col5:
                st.image("default.png")
        with st.container():
            col6,col7,col8 = st.columns([120,120,120])
            with col6:
                st.image("default.png")
            with col7:
                st.image("default.png")
            with col8:
                st.image("default.png")
        
    with col2:
        st.image("default.png")
        st.image("default.png")
