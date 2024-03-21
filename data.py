import streamlit as st
# pip install streamlit
from google.oauth2 import service_account
# pip install google_oauth2_tool
from google.cloud import bigquery, bigquery_storage
#pip install google-cloud-bigquery


from queries import cdf, download

project_id = 'measurement-lab'
location = 'US'
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(project=project_id, location=location,credentials=credentials)


# bq_client = bigquery.Client(project=project_id, location=location,credentials=credentials)
# bq_storage_client = bigquery_storage.BigQueryReadClient(credentials=credentials)
# query_job = bq_client.query(download.query)
# print(query_job)
# query_results = query_job.result()
# print(query_results)
# df = query_results.to_dataframe(bqstorage_client=bq_storage_client)
# print(df)
# df.to_csv('data/download1.csv', index=False)

df = client.query(cdf.query).to_dataframe()
df.to_csv('data/cdf.csv', index=False)

# df = client.query(download.query).to_dataframe()
# df.to_csv('data/download.csv', index=False)


