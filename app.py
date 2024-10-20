import streamlit as st
from time import sleep
import time
import requests

st.set_page_config("Streamlit Simultaneous Process", layout="wide")


def run():
    container = st.container()
    code = st.container()
    with st.expander("Code", expanded=False):
        with st.echo():

            def long_running_process(loops: int, sleep_seconds: int):
                placeholder = st.empty()
                progress_text = "Operation in progress. Please wait."
                my_bar = st.progress(0, text=progress_text)
                for i in range(loops):
                    percent_complete = int((i + 1) / loops * 100)
                    time.sleep(sleep_seconds)
                    my_bar.progress(percent_complete, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                placeholder.write("Long Running Process Complete!")

            col_1, spacer, col_2 = container.columns([2, 1, 2])
            with col_1:
                loops = st.number_input("Loops", value=10)
                sleep_seconds = st.number_input("Sleep Seconds Per Loop", value=1)
                if st.button("Start Longing Running Process"):
                    long_running_process(loops, sleep_seconds)
            with col_2:
                api_delay = st.number_input(
                    "API Delay (seconds)", value=0, min_value=0, max_value=5
                )
                if st.button("Execute API Call"):
                    response = requests.get(
                        f"https://dummyjson.com/products?delay={api_delay*1000}"
                    )
                    if response.status_code == 200:
                        data = response.json()
                        if "products" in data:
                            st.write("API Call Successful!")
                            products = data["products"]
                            st.json(products, expanded=False)
                            st.button("Clear API Response")


run()
