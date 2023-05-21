public class Main {
    public static void main(String[] args) {
        Input input = new Input();
        Something smth = new Something(input.numbers());
        System.out.println(smth.sum());
    }
}
