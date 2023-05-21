import java.util.Arrays;
import java.util.Random;

public class List {
    private final int size;
    private final int [] array;
    private int max = 0;
    private int indexOfMax;
    public List(final int size) {
        this.size = size;
        array = new int[size];
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(10);
        }
    }
    @Override
    public String toString() {
        return Arrays.toString(array);
    }

    public int findMax() {
        for (int i = 0; i < size; i++) {
            if (array[i] > max) {
                max = array[i];
                indexOfMax = i;
            }
        }
        return max;
    }
    public int [] leftOfMax() {
        return Arrays.copyOfRange(array, 0, indexOfMax);
    }
    public void getLeftList() {
        System.out.println(Arrays.toString(leftOfMax()));
    }
    public int [] rightOfMax() {
        return Arrays.copyOfRange(array, indexOfMax + 1, size);
    }
    public void getRightList() {
        System.out.println(Arrays.toString(rightOfMax()));
    }
}
