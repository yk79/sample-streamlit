import json
import streamlit as st
import requests
import pandas as pd
import numpy as np

# import time

st.title("Sample Streamlit")
st.divider()

menu_selectbox = st.sidebar.selectbox(
    "menu",
    ("csv aggregate", "map"),
    index = None
)

print(menu_selectbox)
if menu_selectbox == "csv aggregate":
    st.subheader("sample csv aggregate")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        headers = list(df)
        axis_select = st.selectbox("axis", headers,index = None)
        target_select = st.selectbox("target", headers,index = None)
        if axis_select is not None and target_select is not None:
            values = pd.crosstab(df[axis_select], df[target_select]).apply(lambda r: r/r.sum(), axis=1)
            print(values)
            st.bar_chart(values)
elif menu_selectbox == "map":
    st.subheader("sample map")
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [35.76, 139.4],
        columns=['lat', 'lon']
    )
    st.map(df)
else:
    st.subheader("chose menu")

