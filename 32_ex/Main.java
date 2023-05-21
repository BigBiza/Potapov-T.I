import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long numberOfSticks = scanner.nextLong();
        boolean sashaTurn = true;
        while (numberOfSticks > 1) {
            if (numberOfSticks % 2 == 0) {
                if (sashaTurn) {
                    numberOfSticks /= 2;
                } else {
                    numberOfSticks -= 1;
                }
            } else {
                numberOfSticks -= 1;
            }
            sashaTurn = !sashaTurn;
        }
        if (sashaTurn) {
            System.out.println("Таня проигрывает");
        } else {
            System.out.println("Саша проигрывает");
        }
    }
}
