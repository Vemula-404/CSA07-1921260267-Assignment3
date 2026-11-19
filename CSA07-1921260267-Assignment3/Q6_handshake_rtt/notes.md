# Q6 – Handshake RTTs

| Stack | RTTs | TTFB (100 ms RTT) |
|---|---|---|
| TCP + TLS 1.2 | 3 | 300 ms |
| TCP + TLS 1.3 | 2 | 200 ms |
| QUIC first visit | 1 | 100 ms |
| QUIC 0-RTT | 0 | 0 ms |

## 0-RTT replay risk
Pre-shared key replay → server may re-process request.
Never send non-idempotent (money transfer, password change, OTP) in 0-RTT.
Only GET of static resources.

## QUIC Connection ID
Identifies connection independent of 4-tuple → survives Wi-Fi↔5G IP change.
TCP breaks on IP change → full re-handshake (1 RTT + TLS).

## QUIC blocked by firewall
Many enterprises block UDP 443 (no traditional TLS inspection).
Stack falls back to TCP + TLS 1.3 (HTTP/2) — Happy Eyeballs, ~200 ms.

## Bank verdict
Use QUIC (saves 100 ms per setup + 100 ms per Wi-Fi↔5G transition).
Strict 0-RTT policy: only idempotent GETs.
Fallback to TCP+TLS 1.3 where UDP 443 blocked.