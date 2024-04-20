import streamlit as st

st.set_page_config(layout="wide")

with st.sidebar:
        st.image("default.png")
        st.button(label="input1")
        st.text_input(label="input0")
        st.checkbox(label="input11")
st.title("Template streamlit app")
st.divider()
with st.container():
        col1, col0, col2, col3, col4, col5 = st.columns([100, 240, 100, 130, 130, 130])
        with col1:
        with col0:
                st.image("default.png")
        with col2:
        with col3:
                st.button(label="input3")
        with col4:
                st.button(label="input4")
        with col5:
                st.button(label="input5")