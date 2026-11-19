def simulate(losses, ssthresh=16, reno=True):
    cwnd, trace = 1, []
    for rtt in range(1, 21):
        trace.append(cwnd)
        if rtt in losses:
            ssthresh = max(cwnd // 2, 2)
            cwnd = ssthresh if reno else 1
        else:
            if cwnd < ssthresh:
                cwnd = min(cwnd * 2, ssthresh)
            else:
                cwnd += 1
    return trace


if __name__ == "__main__":
    losses = {8, 14}
    print("Tahoe:", simulate(losses, reno=False))
    print("Reno :", simulate(losses, reno=True))

    # Throughput at RTT 7 (cwnd = 16 segments, MSS 1460, RTT 40 ms)
    cwnd_bytes = 16 * 1460
    thr = cwnd_bytes * 8 / 0.04
    print(f"Throughput @ RTT7 = {thr/1e6:.2f} Mbps")