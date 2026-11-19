# Q5 – M/M/1 Queue & QoS

| Load (pkt/s) | ρ | L | W (ms) |
|---|---|---|---|
| 500 | 0.50 | 1.0 | 2.0 |
| 800 | 0.80 | 4.0 | 5.0 |
| 900 | 0.90 | 9.0 | 10.0 |
| 950 | 0.95 | 19.0 | 20.0 |
| 990 | 0.99 | 99.0 | 100.0 |
| 1000 | 1.00 | ∞ | unstable |

**W > 20 ms first at ρ = 0.95 (950 pkt/s).**
Doubling 450 → 900: W ≈ 1.8 → 10 ms ≈ 5.5×; formula W = 1/(μ-λ) is non-linear.

## Token bucket
Bucket 1 MB = 8 Mbit, rate 2 Mbps, arrival 10 Mbps.
Excess 8 Mbps → burst = 1 s. After 1 s → limited to 2 Mbps.

## DiffServ
| App | DSCP | Why |
|---|---|---|
| Video | EF (46) | low delay, low jitter |
| Backup | AF11 (10) | yields to video |
| Web/email | BE (0) | best effort |

## Engineering decision
W < 10 ms at 950 pkt/s needs μ > 1050 → **5% capacity bump via QoS**, cheaper than new link.

## Alternative – double the link
μ = 2000, load 1800: ρ = 0.9, L = 9, W = 5 ms. Works but costs more than QoS.