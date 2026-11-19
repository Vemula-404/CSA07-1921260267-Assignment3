# Q1 – Socket Demultiplexing

## Demux rules
| Segment | Socket | Reason |
|---|---|---|
| TCP 49.37.2.8:50001 → 203.0.113.5:443 | TCP 443↔49.37.2.8:50001 | 4-tuple match |
| TCP 117.96.4.2:50000 → :443 | TCP 443↔117.96.4.2:50000 | 4-tuple match |
| TCP SYN 106.51.7.7:41000 → :443 | TCP 443 LISTEN | forks new conn |
| UDP 49.37.2.8:50000 → :5004 | UDP :5004 | local-port keyed |

## Same source port 50000 from two hosts
TCP uses full 4-tuple (src IP, src port, dst IP, dst port) → distinct.
UDP socket on 5004 distinguishes viewers by src IP+port in datagram.

## Header overhead (100 B payload)
- UDP: 128 B wire → 21.9% overhead
- TCP: 140 B wire → 28.6% overhead

## Protocol choice per component
| Component | Protocol | Why |
|---|---|---|
| Live scores | UDP / QUIC | stale score useless |
| Commentary | TCP | must be complete + ordered |
| Live video | UDP (RTP) | no HoL stall |

## Loss test results
1% loss → TCP retransmits transparently; UDP loses datagrams.
5% → TCP throughput drops, UDP delivered arrivals.
10% → TCP severe slowdown; UDP loses 10%.

## Verdict
"UDP unreliable" is by design. For live scores, speed > guaranteed delivery.
TCP for final result; UDP for live feed.