import streamlit as st
import pandas as pd

def create_cross():
    uploaded_file = st.file_uploader("Choose a csv file", type="csv")
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