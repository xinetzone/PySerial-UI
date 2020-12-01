from pathlib import Path
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import serial
from serial.tools import list_ports
import time

def read_markdown_file(markdown_file):
    with open(markdown_file, encoding='utf-8') as fp:
        w = fp.read()
    return w



@st.cache
def info2dict(info):
    words = info.strip().split(',')
    words = [word.split(':') for word in words]
    words = {k:v for k, v in words}
    return words

@st.cache
def write_info(data_flow, info, flow_id, save_path='data/data.csv'):
    info_dict = info2dict(info)
    data_flow.loc[flow_id] = info_dict
    data_flow.to_csv(save_path)

def read_until(port, baudrate, timeout, save_path):
    data_flow = pd.DataFrame(columns=['id', 'x', 'y', 'w', 'h', 'd'])
    frame_id = 0
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        # start_time = time.monotonic()
        while 1:
            info = ser.read_until(expected=b'\n')
            info = info.decode()
            st.sidebar.info(info)
            if 'id' in info:
                write_info(data_flow, info, frame_id, save_path)
            frame_id += 1

intro_markdown = read_markdown_file("intro.md")
st.markdown(intro_markdown, unsafe_allow_html=True)


devices = [device for device in list_ports.grep('COM')]
device_names = [str(device) for device in devices]
config_col, table_col = st.beta_columns(2)

with config_col:
    device_name = st.selectbox(label="选择端口设备", options=device_names)
    port_name = device_name.split()[0]
    port = st.text_input('选择了端口:', key='port', value=port_name)
    timeout = st.text_input('超时', key='timeout', value=15)
    baud = st.text_input('波特率', key='baud', value=921600) # 设置波特率

save_path = 'data/data.csv'
if st.sidebar.button('串口信息'):
    st.sidebar.markdown("## 读取结果：")
    st.sidebar.info(f"{port, baud, timeout}")
    read_until(port, baud, int(timeout), save_path)

# @st.cache
def plot_frame(data_iter):
    for frame_id, x in data_iter:
        ax, _ = plt.subplots(1, 1)
        direct = x['d']
        plt.title(f'id: {frame_id}')
        plt.plot(direct)
        st.pyplot(ax)

with table_col:
    with st.beta_expander('显示数据表'):
        from pathlib import Path
        _save_path = Path(save_path)
        if _save_path.exists():
            data_flow = pd.read_csv(save_path)
            st.write(data_flow)


with st.beta_expander('显示数据图'):
    from pathlib import Path
    _save_path = Path(save_path)
    if _save_path.exists():
        data_flow = pd.read_csv(save_path)
        data_iter = data_flow.groupby(by='id')
        plot_frame(data_iter)