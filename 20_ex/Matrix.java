import java.util.Arrays;

public class Matrix {
    private final int[][] matrix;
    public Matrix(int height, int length) {
        matrix = new int[height][length];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < length; j++) {
                int ring = Math.min(Math.min(i, j), Math.min(height-i-1, length-j-1)) + 1;
                matrix[i][j] = ring;
            }
        }
    }
    @Override
    public String toString() {
        return Arrays.deepToString(matrix)
                .replace("[[", "[")
                .replace("], ", "]\n")
                .replace("]]", "]");
    }
}
