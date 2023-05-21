public class Main {
    public static void main(String[] args) {
        Input input = new Input();
        checkBrackets brackets = new checkBrackets(input.getInfo());
        System.out.println(brackets.check());
    }
}
