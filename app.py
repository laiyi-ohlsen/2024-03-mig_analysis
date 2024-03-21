import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('data/cdf.csv')

fig = px.line(df, x="xleft", 
              y="data", 
              color="site",
              log_x=True,
              title="CDF of MIG & VMs over Trial")

st.plotly_chart(fig)

df = pd.read_csv('data/results.csv')
st.table(df)