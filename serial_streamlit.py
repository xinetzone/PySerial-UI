from pathlib import Path
import streamlit as st
import serial
from serial.tools import list_ports

def read_markdown_file(markdown_file):
    with open(markdown_file, encoding='utf-8') as fp:
        w = fp.read()
    return w

intro_markdown = read_markdown_file("intro.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

devices = list(list_ports.grep('COM'))
device_names = [str(device) for device in devices]

device_name = st.selectbox(label="选择端口设备", options=device_names)
device_name = device_name.split()[0]