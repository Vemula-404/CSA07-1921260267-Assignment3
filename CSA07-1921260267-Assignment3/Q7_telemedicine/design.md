# Q7 – Telemedicine Protocol Design

## Stage 1 – Requirements
| Traffic | Delay | Loss | Order | Security |
|---|---|---|---|---|
| Live video | <150 ms | some OK | per-stream | DTLS/SRTP |
| Records | <2 s | none | in-order | TLS 1.3 |
| X-ray | <10 s | none | in-order | TLS 1.3 |
| Chat | <500 ms | none | in-order | TLS 1.3 |
| DNS | <100 ms | retry | in-order | DNSSEC |

Measurable: P95 video <150 ms; X-ray <10 s @5% loss; chat P95 <500 ms.

## Stage 2 – Protocol comparison
| Stack | Video | Files | Chat |
|---|---|---|---|
| TCP+TLS1.3 | poor | good | good |
| UDP+WebRTC | best | manual rel | possible |
| QUIC HTTP/3 | good | excellent | excellent |
| HTTP/2 | poor | good | good |

TCP limit @ 64 KB window, 300 ms RTT: ≈ 1.75 Mbps → 5–20 MB X-ray takes 2.5–12 s.
Window scaling (4 MB) → ~110 Mbps.

## Stage 3 – Implementation
- File: Python TCP socket; `tc netem delay 200ms loss 5%`
- Chat: aioquic or UDP + sequence numbers
- Measured: 5 MB file 8 s (TCP) vs 3 s (QUIC) @5% loss
- Video: WebRTC (UDP) — no freeze @1%, glitch @5%

## Stage 4 – Final choice
| Traffic | Protocol | Why |
|---|---|---|
| Live video | UDP + WebRTC | no HoL blocking |
| Records / X-ray / chat | QUIC | fast loss recovery + TLS 1.3 |
| DNS | DNSSEC UDP (TCP large) | fast, cacheable |

**5G upgrade:** TCP+TLS 1.3 becomes viable for files/chat (20–50 ms, <0.5% loss).
QUIC still best for mobility. Keep WebRTC for video, simplify chat to HTTP/3.

## Commercial video service – due-diligence questions
1. P95 latency budget?
2. Encryption in transit + at rest? Server location?
3. Loss recovery: FEC / ARQ / both?
4. SLA for rural 4G?
5. Data residency for recordings?
Require independent P95 measurements, ISO 27001 / HIPAA-equivalent, no data leaving country.
Without those → in-house WebRTC + QUIC is safer.