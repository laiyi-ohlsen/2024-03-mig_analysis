import pandas as pd
import numpy as np
from scipy import stats


dfs = {
    'dl_filtered_raw': pd.read_csv('data/dl_filtered_raw.csv'),
    'dl_filtered_cdf': pd.read_csv('data/dl_filtered_cdf.csv'),
    'dl_unfiltered_raw': pd.read_csv('data/dl_unfiltered_raw.csv'), 
    'dl_unfiltered_cdf': pd.read_csv('data/dl_unfiltered_cdf.csv'),
    'ul_filtered_raw': pd.read_csv('data/ul_filtered_raw.csv'),
    'ul_filtered_cdf': pd.read_csv('data/ul_filtered_cdf.csv'),
    'ul_unfiltered_raw': pd.read_csv('data/ul_unfiltered_raw.csv'),
    'ul_unfiltered_cdf': pd.read_csv('data/ul_unfiltered_cdf.csv'),
    'both_unfiltered_raw': pd.read_csv('data/both_unfiltered_raw.csv'),
    'both_unfiltered_cdf': pd.read_csv('data/both_unfiltered_cdf.csv')
}

VMs = ['del03', 'hnd06', 'iad07', 'lhr09', 'scl05', 'syd07']
MIGs =  ['del05', 'hnd07', 'iad09', 'lhr10', 'scl06', 'syd08']

def geo_mean(site):
    # Filter out 0s
    site = site.loc[site['download'] > 0]
    # get log(x) base10 or log(download) 
    site['download_log'] = np.log10(site['download'])
    # get mean(log(x))
    site_mean_log_x = np.mean(site['download_log'])
    # get geo _mean
    site_geo_mean = np.power(10, site_mean_log_x)
    return site_geo_mean

# def geo_distance(site1_geo_mean, site2_geo_mean):
#     return site1_geo_mean / site2_geo_mean

# def get_geo_results(df1, df2): 
#     site1_dl_filtered_geomean = geo_mean(df1)
#     site2_dl_filtered_geomean = geo_mean(df2)


def generate_table(direction, filter): 
    d = pd.DataFrame()
    for x, site in enumerate(VMs):
        site1 = site; 
        site2 = MIGs[x]
        print(site1 +", "+ site2)
        raw_ = "{}_{}_raw".format(direction,filter)
        print(raw_)
        cdf_= "{}_{}_cdf".format(direction,filter)
        print(cdf_)

        raw = dfs[raw_]
        cdf = dfs[cdf_]

        site1_raw = raw.loc[raw['site'] == site1]
        print(site1_raw)
        site2_raw = raw.loc[raw['site'] == site2]
        site1_cdf = cdf.loc[cdf['site'] == site1]['data'].values.tolist()
        site2_cdf = cdf.loc[cdf['site'] == site2]['data'].values.tolist()

        site1_geo_mean, site2_geo_mean, geodistance1, geodistance2,ks_statistic = calc_stats(site1_raw,site2_raw,site1_cdf,site2_cdf)

        site1_testcount = len(site1_raw.index)
        site2_testcount = len(site2_raw.index)
       
        d.loc[x, 'MIG'] = site1 
        d.loc[x, 'VM'] =  site2 
        d.loc[x, 'MIG test count'] = site1_testcount
        d.loc[x, 'VM test count'] = site2_testcount
        d.loc[x, 'KS Statistic'] =  ks_statistic
        d.loc[x, 'MIG geo mean'] = site1_geo_mean 
        d.loc[x, 'VM geo mean'] = site2_geo_mean 
        d.loc[x, 'Geo distance (MIG/VM)'] = geodistance1
        d.loc[x, 'Geo distance (VM/MIG)'] = geodistance2

    return d
            

def calc_stats(site1_raw, site2_raw, site1_cdf, site2_cdf):
    site1_geo_mean = geo_mean(site1_raw)
    site2_geo_mean = geo_mean(site2_raw)

    geodistance1 = site1_geo_mean / site2_geo_mean
    geodistance2 = site2_geo_mean / site1_geo_mean

    ks_statistic =  stats.ks_2samp(site1_cdf,site2_cdf).statistic

    return site1_geo_mean, site2_geo_mean, geodistance1, geodistance2, ks_statistic

def generate_results(d,f):
    results = generate_table(d, f)
    file = 'data/{}_{}_results.csv'.format(d,f)
    results.to_csv(file, index=False)



def generate_all():
    directions = ["dl", "ul"]
    filters = ["filtered", "unfiltered"]
    for d in directions:
        print(d)
        for f in filters: 
            generate_results(d,f)


generate_all()

generate_results("both","unfiltered")