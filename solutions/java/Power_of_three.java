package PowerOfThree;

import java.util.Scanner;

public class Main {

    public static long powerMod(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1)
                result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }

    public static int isPowerOfThree(String N) {
        if (N.equals("0")) return -1;
        if (N.equals("1")) return 0;

        N = N.replaceFirst("^0+(?!$)", "");

        int len = N.length();

        int lastDigit = N.charAt(len - 1) - '0';
        if (lastDigit != 1 && lastDigit != 3 && lastDigit != 7 && lastDigit != 9)
            return -1;

        int remainder = 0;
        for (int i = 0; i < len; i++) {
            remainder = (remainder * 10 + (N.charAt(i) - '0')) % 3;
        }
        if (remainder != 0) return -1;

        double estimatedPower = (len - 1) / 0.47712125471966244;
        int startPower = (int) (estimatedPower - 1);
        if (startPower < 0) startPower = 0;

        final int MOD1 = 1000000007;
        final int MOD2 = 998244353;

        long rem1 = 0, rem2 = 0;
        for (int i = 0; i < len; i++) {
            rem1 = (rem1 * 10 + (N.charAt(i) - '0')) % MOD1;
            rem2 = (rem2 * 10 + (N.charAt(i) - '0')) % MOD2;
        }

        for (int x = startPower; x <= startPower + 3; x++) {
            int powerLength = (int) (x * 0.47712125471966244) + 1;
            if (powerLength != len) continue;

            if (powerMod(3, x, MOD1) == rem1 && 
                powerMod(3, x, MOD2) == rem2) {
                return x;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String N = scanner.next();
        System.out.println(isPowerOfThree(N));
        scanner.close();
    }
}