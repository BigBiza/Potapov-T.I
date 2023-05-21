import java.util.ArrayList;
public class Something {
    private final  int [] a;
    private final  int [] b;
    public Something(ArrayList<Integer> array) {
        a = new int[array.get(1)-array.get(0)+1];
        for (int i = 0; i < array.get(1)-array.get(0)+1; i++) {
            a[i] = array.get(0) + i;
        }
        b = new int[array.size()-2];
        for (int i = 2; i < array.size(); i++) {
            b[i-2] = array.get(i);
        }
    }

    public int sum() {
        int sum = 0;
        for (int i : a) {
            for (int j : b) {
                if (i % j == 0) {
                    sum += i;
                }
            }
        }
        return sum;
    }
}
