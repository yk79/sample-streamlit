import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def create_plot(df: pd.DataFrame, x_column: str, y_column: str, z_column: str = None, label: str = None):
    if z_column:
        return px.scatter_3d(
            df,
            x_column,
            y_column,
            z_column,
            text=label,
            hover_name=label,
            height=700,
            width=700,
            color="スコア"
        )
    else:
        return px.scatter(
            df,
            x_column,
            y_column,
            color="スコア",
            text=label,
            hover_name=label
        )


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
            df["スコア"] = df.apply(lambda row: row[x_column] + row[y_column] + (row[z_column] if z_column else 0), axis=1)
            st.plotly_chart(create_plot(df, x_column, y_column, z_column, label))
