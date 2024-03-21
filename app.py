import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/cdf.csv')

fig = px.line(df, x="xleft", 
              y="data", 
              color="site",
              log_x=True,
              title="CDF of MIG & VMs over Trial")
st.plotly_chart(fig)