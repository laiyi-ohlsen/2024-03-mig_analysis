import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

dl_filtered_cdf = pd.read_csv('data/dl_filtered_cdf.csv')
dl_filtered_results = pd.read_csv('data/dl_filtered_results.csv')
dl_unfiltered_cdf = pd.read_csv('data/dl_unfiltered_cdf.csv')
dl_unfiltered_results = pd.read_csv('data/dl_unfiltered_results.csv')
ul_filtered_cdf = pd.read_csv('data/ul_filtered_cdf.csv')
ul_filtered_results = pd.read_csv('data/ul_filtered_results.csv')
ul_unfiltered_cdf = pd.read_csv('data/ul_unfiltered_cdf.csv')
ul_unfiltered_results = pd.read_csv('data/ul_unfiltered_results.csv')


tab1, tab2, tab3,tab4 = st.tabs(["Download Filtered", 
                            "Download Unfiltered", 
                            "Upload Filtered", 
                            "Upload Unfiltered"])

with tab1: 
    st.header("Download Filtered")
    fig = px.line(dl_filtered_cdf, x="xleft", 
                y="data", 
                color="site",
                log_x=True)

    st.plotly_chart(fig)

    df = pd.read_csv('data/dl_filtered_results.csv')
    st.table(df)

with tab2: 

    st.header("Download Unfiltered")
    fig = px.line(dl_unfiltered_cdf, x="xleft", 
                y="data", 
                color="site",
                log_x=True)

    st.plotly_chart(fig)

    df = pd.read_csv('data/dl_unfiltered_results.csv')
    st.table(df)

with tab3: 

    st.header("Upload Filtered")
    fig = px.line(ul_filtered_cdf, x="xleft", 
                y="data", 
                color="site",
                log_x=True)

    st.plotly_chart(fig)

    df = pd.read_csv('data/ul_filtered_results.csv')
    st.table(df)

with tab4: 

    st.header("Upload Unfiltered")
    fig = px.line(ul_unfiltered_cdf, x="xleft", 
                y="data", 
                color="site",
                log_x=True)

    st.plotly_chart(fig)

    df = pd.read_csv('data/ul_unfiltered_results.csv')
    st.table(df)