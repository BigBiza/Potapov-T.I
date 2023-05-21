import java.util.ArrayList;
import java.util.Collections;

public class GradeSum {
    private final int number;
    private int x;
    private final ArrayList<Integer> digits = new ArrayList<>();

    public GradeSum(int number, int x) {
        this.number = number;
        this.x = x;
        int temp = number;
        while (temp > 0) {
            digits.add(temp % 10);
            temp /= 10;
        }
        Collections.reverse(digits);
    }
    public boolean find() {
        int sum = 0;
        int [] a = new int[digits.size()];
        for (int i = 0; i < digits.size(); i++) {
            a[i] = x;
            sum += digits.get(i);
            x++;
        }
        boolean b = false;
        for (int j : a) {
            if (sum % j == 0) {
                b = true;
                break;
            } else {
                b = false;
            }
        }
        return b;
    }
}
