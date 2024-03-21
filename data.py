import streamlit as st
# pip install streamlit
from google.oauth2 import service_account
# pip install google_oauth2_tool
from google.cloud import bigquery
#pip install google-cloud-bigquery


from queries import cdf

project_id = 'measurement-lab'
location = 'US'
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(project=project_id, location=location,credentials=credentials)

df = client.query(cdf.query).to_dataframe()
df.to_csv('data/cdf.csv', index=False)