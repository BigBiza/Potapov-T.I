import java.util.ArrayList;
import java.util.Arrays;

public class Voyage {
    private final int petrol;
    private final int number;
    private final int[] array;
    private ArrayList<int[]> combinations;

    public Voyage(int petrol, int number, int[] array) {
        this.petrol = petrol;
        this.number = number;
        this.array = array;
        combinations = getCombinations(array, number);
    }
    public void bestWay(){
        int maxSum = -1;
            for (int[] combo : combinations) {
            int sum = Arrays.stream(combo).sum();
            if (sum <= petrol && sum > maxSum) {
                maxSum = sum;
            }
        }
            System.out.println(maxSum);
    }
    public ArrayList<int[]> getCombinations(int[] arr, int n) {
        ArrayList<int[]> res = new ArrayList<>();
        int[] combo = new int[n];
        combinationsHelper(res, arr, combo, 0, 0);
        return res;
    }
    public void combinationsHelper(ArrayList<int[]> res, int[] arr, int[] combo, int index, int start) {
        if (index == combo.length) {
            res.add(Arrays.copyOf(combo, combo.length));
        } else {
            for (int i = start; i < arr.length; i++) {
                combo[index] = arr[i];
                combinationsHelper(res, arr, combo, index + 1, i + 1);
            }
        }
    }
}
