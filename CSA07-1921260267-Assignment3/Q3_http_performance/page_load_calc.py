RTT = 0.050   # 50 ms
objs = 80

def rtts_nonpersistent_serial(n):   return 1 + 2*n
def rtts_persistent_no_pipe(n):     return 1 + n
def rtts_persistent_pipe(n):        return 2
def rtts_parallel_nonpersistent(n, k=6): return 1 + 2*(n/k)

for name, r in [
    ("Non-persistent serial",       rtts_nonpersistent_serial(objs)),
    ("Persistent no pipelining",    rtts_persistent_no_pipe(objs)),
    ("Persistent + pipelining",     rtts_persistent_pipe(objs)),
    ("6 parallel non-persistent",   rtts_parallel_nonpersistent(objs)),
]:
    print(f"{name:30s} {r:6.1f} RTT -> {r*RTT:6.2f} s")

# Bundle 80 -> 8
print("\nBundle 80 -> 8 objects:")
print(f"  Non-persistent: {(1+2*8)*RTT:.2f} s")
print(f"  Persistent:     {(1+8)*RTT:.2f} s")