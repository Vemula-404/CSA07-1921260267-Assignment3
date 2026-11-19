bucket_bits = 1 * 1024 * 1024 * 8      # 1 MB
rate_bps    = 2_000_000
arrival_bps = 10_000_000

excess = arrival_bps - rate_bps
burst  = bucket_bits / excess
print(f"Excess = {excess/1e6:.0f} Mbps, burst = {burst:.0f} s before limiter kicks in")