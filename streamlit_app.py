from pathlib import Path
import streamlit as st
import serial

def read_markdown_file(markdown_file):
    with open(markdown_file, encoding='utf-8') as fp:
        w = fp.read()
    return w

intro_markdown = read_markdown_file("intro.md")
st.markdown(intro_markdown, unsafe_allow_html=True)


