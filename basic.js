function linearCongGenerator(r0, a, c, m, n) {
  let r = r0;
  for (let i = 0; i < n; i++) {
    r = (a * r + c) % m;
  }
  return r;
}
