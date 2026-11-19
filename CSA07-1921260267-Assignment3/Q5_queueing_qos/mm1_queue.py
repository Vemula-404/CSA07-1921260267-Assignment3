def mml(lam, mu):
    if lam >= mu:
        return None
    rho = lam / mu
    L = rho / (1 - rho)
    W = 1 / (mu - lam)        # seconds
    return rho, L, W


if __name__ == "__main__":
    mu = 1000
    print(f"{'load':>5} {'rho':>5} {'L':>6} {'W(ms)':>8}")
    for lam in (500, 800, 900, 950, 990, 1000):
        r = mml(lam, mu)
        if r is None:
            print(f"{lam:5d}  1.00    inf  unstable")
        else:
            rho, L, W = r
            print(f"{lam:5d} {rho:5.2f} {L:6.1f} {W*1000:8.1f}")