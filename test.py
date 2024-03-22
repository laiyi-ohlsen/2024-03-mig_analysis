import pandas as pd
import numpy as np
from scipy import stats

dl_filtered_raw = pd.read_csv('data/dl_filtered_raw.csv'),
# dl_filtered_raw = pd.DataFrame()
dl_filtered_cdf = pd.read_csv('data/dl_filtered_cdf.csv')
# dl_unfiltered_raw = pd.DataFrame()
# dl_unfiltered_cdf = pd.DataFrame()
# ul_filtered_raw = pd.DataFrame()
# ul_filtered_cdf = pd.DataFrame()
# ul_unfiltered_raw = pd.DataFrame()
# ul_unfiltered_cdf = pd.DataFrame()

dfs = {
    'dl_filtered_raw': pd.read_csv('data/dl_filtered_raw.csv'),
    'dl_filtered_cdf': pd.read_csv('data/dl_filtered_cdf.csv')
    # 'dl_unfiltered_raw': dl_unfiltered_raw, 
    # 'dl_unfiltered_cdf': dl_unfiltered_cdf,
    # 'ul_filtered_raw': ul_filtered_raw,
    # 'ul_filtered_cdf': ul_filtered_cdf,
    # 'ul_unfiltered_raw': ul_unfiltered_raw,
    # 'ul_unfiltered_cdf': ul_unfiltered_cdf
}


raw_ = "{}_{}_raw".format("dl", "filtered")
cdf_ = "{}_{}_cdf".format("dl", "filtered")
print(cdf_)

raw = dfs[raw_]

print(type(raw))