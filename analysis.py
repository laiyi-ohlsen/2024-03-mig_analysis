import pandas as pd
import numpy as np

df = pd.read_csv('data/download.csv')


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


def geo_distance(site1_geo_mean, site2_geo_mean):
    return site1_geo_mean / site2_geo_mean

def get_results(): 
    d = pd.DataFrame()
    for x, site in enumerate(VMs):
        site1 = df.loc[df['site'] == site]
        site2 = df.loc[df['site'] == MIGs[x]]

        site1_geo_mean = geo_mean(site1)
        site2_geo_mean = geo_mean(site2)

        geo_distance = site1_geo_mean / site2_geo_mean

        d.loc[x, 'MIG'] = site; 
        d.loc[x, 'VM'] =  MIGs[x]; 
        d.loc[x, 'MIG geo mean'] = site1_geo_mean; 
        d.loc[x, 'VM geo mean'] = site2_geo_mean; 
        d.loc[x, 'Geo distance (MIG/VM)'] = geo_distance; 
    return d

results = get_results()
print(results)
results.to_csv('data/results.csv', index=False)
