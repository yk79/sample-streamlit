import streamlit as st
import pandas as pd
import plotly.express as px

def create_plot(df: pd.DataFrame, x_column: str, y_column: str, z_column: str = None, label: str = None):
    if z_column:
        return px.scatter_3d(df, x_column, y_column, z_column, text=label, hover_name=label, height=700, width=700, color_continuous_midpoint=px.colors.qualitative.swatches())
    else:
        return px.scatter(df, x_column, y_column)


def create_scatter_plot():
    uploaded_file = st.file_uploader("Choose a csv file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        columns = df.columns.tolist()
        label = st.selectbox("Please select label", columns, index = None)
        x_column = st.selectbox("Please select x-axis", columns, index = None)
        y_column = st.selectbox("Please select y-axis", columns, index = None)
        z_column = st.selectbox("Please select z-axis", columns, index = None)
        if x_column and y_column:
            st.plotly_chart(create_plot(df, x_column, y_column, z_column, label))
