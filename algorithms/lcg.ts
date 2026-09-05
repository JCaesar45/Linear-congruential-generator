interface LCGParams {
    r0: number;
    a: number;
    c: number;
    m: number;
    n: number;
}

function linearCongGenerator(r0: number, a: number, c: number, m: number, n: number): number {
    let r: number = r0;
    for (let i: number = 0; i < n; i++) {
        r = (a * r + c) % m;
    }
    return r;
}

export { linearCongGenerator, LCGParams };
