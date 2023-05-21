public class Difference {
    private final int number;

    public Difference(int number) {
        this.number = number;
    }
    public void find() {
        int diff;
        boolean t = false;
        for (int i = 0; i < number; i++) {
            int y = i + 1;
            diff = y * y - i * i;
            if (diff == number) {
                t = true;
                break;
            }
        }
        System.out.println(t);
    }
}
