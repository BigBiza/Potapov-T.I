import java.util.ArrayList;
import java.util.Scanner;

public class Input {
    public ArrayList<Integer> numbers() {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        int i = -1;
        do {
            i++;
            numbers.add(scanner.nextInt());
        } while (numbers.get(i) != 0);
        numbers.remove(i);
        return numbers;
    }
}