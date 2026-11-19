# Q4 – DNS Queries

## Query counts (40 resolvers)
| TTL | Refreshes/h | Total queries/h |
|---|---|---|
| 300 s | 12 | 480 |
| 60 s | 60 | 2,400 |
| 30 s | 120 | 4,800 |

Students = 150,000 is irrelevant — resolvers cache for all their students.

## Recursive vs iterative
Phone → Resolver: **recursive**.
Resolver → Root → .in → ac.in → simats: **iterative** referrals.

## Record types
A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), NS (auth NS), TXT (SPF/DKIM).
UDP for small queries; TCP when response > 512 B (DNSSEC, many records).

## Long-TTL risk
86400 s TTL → old IP cached up to 24 h → result-day server move fails.
Result day: TTL 60 s. Normal: 300 s.

## Setup decision
A + AAAA + CNAME + NS + MX + TXT. Two auth NS at different providers.
TTL 60 s during result event → 2,400 queries/h — trivial.

## Anycast CDN alternative
Query goes to nearest CDN PoP → 0 queries to university server, 10–30 ms lookup.