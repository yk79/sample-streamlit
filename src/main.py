import json
import streamlit as st
import requests
import pandas as pd
import numpy as np

from chart.cross import create_cross
from chart.map import create_map
from chart.scatterPlot import create_scatter_plot

st.title("Sample Streamlit")
st.divider()

menu_selectbox = st.sidebar.selectbox(
    "menu",
    ("simple cross", "scatter plot" ,"map"),
    index = None
)

print(menu_selectbox)
if menu_selectbox == "simple cross":
    st.subheader("sample cross")
    create_cross()
elif menu_selectbox == "scatter plot":
    st.subheader("scatter plot")
    create_scatter_plot()
elif menu_selectbox == "map":
    st.subheader("sample map")
    create_map()
else:
    st.subheader("chose menu")


# st.write("このサービスは、政府統計総合窓口(e-Stat)のAPI機能を使用していますが、サービスの内容は国によって保証されたものではありません。")
