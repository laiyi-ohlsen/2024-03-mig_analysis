query=f'''
SELECT
  server.Site as site,
  date, 
  a.MeanThroughputMbps as download
FROM `measurement-lab.ndt_intermediate.extended_ndt7_uploads`
WHERE DATE BETWEEN '2024-01-01' AND '2024-03-31'
AND server.Site IN (
  'del03', 'del05',
  'hnd06', 'hnd07',
  'iad07', 'iad08', 'iad09',
  'lhr09', 'lhr10',
  'scl05', 'scl06',
  'syd07', 'syd08'
  )
AND (filter.IsComplete -- Not missing any important fields
      AND filter.IsProduction -- not a test server
      AND NOT filter.IsError -- Server reported an error
      AND NOT filter.IsOAM -- operations and management traffic
      AND NOT filter.IsPlatformAnomaly -- overload, bad version, etc
      AND NOT filter.IsSmall -- less than 8kB data
      AND (NOT filter.IsShort OR filter.IsEarlyExit) -- insufficient duration or early exit.
      AND NOT filter.IsLong -- excessive duraton
      -- TODO(https://github.com/m-lab/k8s-support/issues/668) deprecate? _IsRFC1918
      AND NOT filter._IsRFC1918)
      '''