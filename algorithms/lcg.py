def linear_cong_generator(r0: int, a: int, c: int, m: int, n: int) -> int:
    r = r0
    for _ in range(n):
        r = (a * r + c) % m
    return r
