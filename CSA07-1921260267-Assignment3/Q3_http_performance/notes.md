# Q3 – HTTP Performance

| Mode | RTTs | Time |
|---|---|---|
| Non-persistent serial | 161 | 8.05 s |
| Persistent HTTP/1.1 | 81 | 4.05 s |
| Persistent + pipelining | 2 | 0.10 s |
| 6 parallel non-persistent | ~27.7 | 1.39 s |

## HTTP/2 HoL blocking
One TCP connection, one lost segment stalls all streams (≥1 RTT).
HTTP/3 (QUIC) = per-stream recovery → no cross-stream stall.

## Cache headers
`Cache-Control: max-age=86400` → second visit within a day: 0 requests.
`ETag` → 304 Not Modified = 1 RTT instead of full download.

## Devtools experiment
HTTP/2, 6 connections, 1.2 s first load.
+50 ms delay → 1.8 s; +200 ms → 6.1 s; warm cache → 50 ms.

## Ranking of changes
| Change | Saving |
|---|---|
| HTTP/3 (QUIC) | ~70% on lossy links |
| Persistent + HTTP/2 | ~50% |
| Cache headers | ~95% on second visit |

## Bundle 80 → 8
Non-persistent: 17 RTT ≈ 0.85 s (90% saving)
Persistent: 9 RTT ≈ 0.45 s
HTTP/2 multiplexed: ~1 RTT ≈ 0.05 s → best