import streamlit as st
import subprocess
import os
import signal
import asyncua


def start_server():
    global process
    process = subprocess.Popen(["python", "server-minimal.py"])
    st.session_state.is_server_on = True
    st.session_state.server_status = "ON"


def stop_server():
    os.kill(process.pid, signal.SIGTERM)
    st.session_state.is_server_on = False
    st.session_state.server_status = "OFF"


if "is_server_on" not in st.session_state:
    st.session_state.is_server_on = False
    st.session_state.server_status = "OFF"

if st.session_state.is_server_on:
    status_color = "green"
else:
    status_color = "red"

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Start Server", on_click=start_server)

with col2:
    st.button("Stop Server", on_click=stop_server)

with col3:
    st.write("Server Status:")
    st.markdown(f"<h1 style='text-align: center; color: {status_color};'>{st.session_state.server_status}</h1>",
                unsafe_allow_html=True)
