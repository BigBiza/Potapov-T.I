import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[][] array = {{5, 2, 8}, {4, 6, 3}, {1, 9, 0}};
        List<Integer> sorted = SnailArraySort.snail(array);
        System.out.println(sorted);
    }
}
