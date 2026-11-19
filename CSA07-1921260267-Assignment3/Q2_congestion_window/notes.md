# Q2 – Congestion Window

## Trace
1,2,4,8,16,17,18,19,9,10,11,12,13,14,1,2,4,...

## ssthresh updates
- Initial 16
- Round 8 loss: ssthresh = max(19/2, 2) = 9, cwnd = 9 (Reno fast recovery)
- Round 14 loss: ssthresh = max(14/2, 2) = 7, cwnd = 1 (timeout / Tahoe)

## Loss types
- Round 8: triple-dup ACK → fast retransmit
- Round 14: timeout → slow start restart

## Reno or Tahoe?
Reno at round 8 (cwnd = 9), timeout at 14 → Reno with a timeout event.

## Throughput @ RTT 7
cwnd = 16 × 1460 B = 23,360 B = 186,880 bits / 0.04 s = **4.67 Mbps**

## AIMD fairness
Both flows +1 per RTT (additive), both halve on loss (multiplicative) → converge to equal share.

## Tahoe vs Reno simulation
Tahoe 144 segments in 20 RTTs; Reno 211 → Reno recovers faster.

## CUBIC vs BBR
- CUBIC: loss-reactive, poor on random-loss wireless
- BBR: bandwidth+RTT estimate, ignores random loss → **BBR recommended for hostel wireless**
- If loss is congestion-driven → CUBIC prevents collapse