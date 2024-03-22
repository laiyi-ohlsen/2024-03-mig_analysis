query=f'''
WITH xbins AS (

  SELECT x, POW(10, x-.01) AS xleft, POW(10, x+.01) AS xright
  FROM UNNEST(GENERATE_ARRAY(-1, 3.5, .02)) AS x

), ndt7 AS (

  SELECT *
  FROM `measurement-lab.ndt.ndt7`
  WHERE ((DATE BETWEEN '2024-01-31' AND '2024-02-06') OR (DATE BETWEEN '2024-02-08' AND '2024-02-14'))
  AND Server.site IN (
  'del03', 'del05',
  'hnd06', 'hnd07',
  'iad07', 'iad08', 'iad09',
  'lhr09', 'lhr10',
  'scl05', 'scl06',
  'syd07', 'syd08'
  )
), ndt7_into_xbins AS (

  SELECT
    xleft, xright, server.Site as site,
    IF(a.MeanThroughputMbps BETWEEN xleft AND xright, 1, 0) AS mbps_present,
  FROM ndt7, xbins

), ndt7_xbins_counts AS (  

  SELECT
    xleft, site,
    SUM(mbps_present) AS mbps_bin_count,
  FROM   ndt7_into_xbins
  GROUP BY xleft, site
  ORDER BY xleft

), ndt7_xbins_counts_site_sum AS (

  SELECT  
    xleft,
    site,
    mbps_bin_count,
    SUM(mbps_bin_count) OVER (partition by site) AS mbps_site_sum,
  FROM ndt7_xbins_counts
  ORDER BY xleft

), pdf_norm AS (

  SELECT
    xleft,
    site,
    mbps_bin_count / mbps_site_sum AS mbps_site_pdf,
  FROM ndt7_xbins_counts_site_sum

), cdf_norm AS (

  SELECT
    xleft,
    site,
    mbps_site_pdf, SUM(mbps_site_pdf) OVER (PARTITION BY site ORDER BY xleft ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS mbps_site_cdf,
  FROM pdf_norm

)

SELECT
  xleft,
  mbps_site_cdf AS data,
  site,

FROM cdf_norm
ORDER BY site ASC
'''