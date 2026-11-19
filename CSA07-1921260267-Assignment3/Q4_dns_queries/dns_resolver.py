SERVERS = {
    'root': {'.': 'tld'},
    'tld':  {'.in': 'sld'},
    'sld':  {'ac.in': 'auth'},
    'auth': {'simats.ac.in': '203.0.113.10'},
}
cache = {}


def resolve(name):
    if name in cache:
        return cache[name], 0
    server, queries = 'root', 0
    while True:
        queries += 1
        keys = sorted(SERVERS[server].keys(), key=len, reverse=True)
        for k in keys:
            if name.endswith(k):
                val = SERVERS[server][k]
                if any(c.isdigit() for c in val):
                    cache[name] = val
                    return val, queries
                server = val
                break
        else:
            return None, queries


if __name__ == "__main__":
    print(resolve("results.simats.ac.in"))
    print(resolve("results.simats.ac.in"))   # cached -> 0 queries