query=f'''
SELECT
  server.Site as site,
  date, 
  a.MeanThroughputMbps as download
FROM `measurement-lab.ndt.ndt7`
WHERE DATE BETWEEN '2024-01-01' AND '2024-03-31'
AND raw.download IS NOT NULL
AND server.Site IN (
  'del03', 'del05',
  'hnd06', 'hnd07',
  'iad07', 'iad08', 'iad09',
  'lhr09', 'lhr10',
  'scl05', 'scl06',
  'syd07', 'syd08'
  )
      '''