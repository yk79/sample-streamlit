import streamlit as st
import pandas as pd
import numpy as np

def create_map():
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [35.76, 139.4],
        columns=['lat', 'lon']
    )
    st.map(df)