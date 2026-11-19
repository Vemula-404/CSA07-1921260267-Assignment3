RTT = 0.100  # 100 ms

stacks = [
    ("TCP + TLS 1.2",              3),
    ("TCP + TLS 1.3",              2),
    ("QUIC first visit",           1),
    ("QUIC 0-RTT resumption",      0),
]
for name, rtts in stacks:
    print(f"{name:25s} {rtts} RTT -> {rtts*RTT*1000:5.0f} ms TTFFB")