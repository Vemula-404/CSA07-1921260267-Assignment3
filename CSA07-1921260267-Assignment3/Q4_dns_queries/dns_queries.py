students = 150_000
resolvers = 40

for ttl in (300, 30, 60):
    refreshes = 3600 // ttl
    per_resolver = refreshes
    total = refreshes * resolvers
    print(f"TTL={ttl:4d}s -> {refreshes:3d} refreshes/h/resolver, total {total} queries/h")