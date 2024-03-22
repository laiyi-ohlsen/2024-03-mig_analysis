query=f'''
SELECT
  server.Site as site,
  date, 
  a.MeanThroughputMbps as download
FROM `measurement-lab.ndt.ndt7`
WHERE ((DATE BETWEEN '2024-01-31' AND '2024-02-06') OR (DATE BETWEEN '2024-02-08' AND '2024-02-14'))
AND server.Site IN (
  'del03', 'del05',
  'hnd06', 'hnd07',
  'iad07', 'iad08', 'iad09',
  'lhr09', 'lhr10',
  'scl05', 'scl06',
  'syd07', 'syd08'
  )
      '''