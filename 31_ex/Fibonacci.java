import java.util.Arrays;
public class Fibonacci {
    public long getFibonacci(int i) {
        double sqrt5 = Math.sqrt(5);
        double phi = (1 + sqrt5) / 2;
        double psi = (1 - sqrt5) / 2;
        return Math.round((Math.pow(phi, i) - Math.pow(psi, i)) / sqrt5);
    }
    public int getMaxDigit(long num) {
        int[] counts = new int[10];
        while (num > 0) {
            counts[(int) (num % 10)]++;
            num /= 10;
        }
        int maxCount = Arrays.stream(counts).max().getAsInt();
        for (int i = 9; i >= 0; i--) {
            if (counts[i] == maxCount) {
                return i;
            }
        }
        return -1;
    }
    public int getCountOfMaxDigit(long num, int digit) {
        int count = 0;
        while (num > 0) {
            if (num % 10 == digit) {
                count++;
            }
            num /= 10;
        }
        return count;
    }
}

