public class Main {
    public static void main(String[] args) {
        Caesar caesar = new Caesar("word", 2, "right");
        System.out.println(caesar.cipher());
    }
}
