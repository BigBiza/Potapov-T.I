public class Something {
    private final int a;
    private final int b;
    private final int c;
    private final int[] array;

    public Something(int a, int b, int c) {
        this.a = a;
        array = new int[a];
        for (int i = 0; i < a; i++) {
            array[i] = i+1;
        }
        this.b = b;
        this.c = c;
    }
    public int sum() {
        int sum = 0;
        for (int i = 0; i < a; i++) {
            if (array[i] % b ==0 || array[i] % c == 0) {
                sum += array[i];
            }
        }
        return sum;
    }
}
