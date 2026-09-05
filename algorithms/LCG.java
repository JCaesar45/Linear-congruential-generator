public class LCG {
    public static long linearCongGenerator(long r0, long a, long c, long m, int n) {
        long r = r0;
        for (int i = 0; i < n; i++) {
            r = (a * r + c) % m;
        }
        return r;
    }

    public static void main(String[] args) {
        System.out.println(linearCongGenerator(324, 1145, 177, 2148, 3));
    }
}
