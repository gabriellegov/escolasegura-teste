import streamlit as st

def localCSS(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

