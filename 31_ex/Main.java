public class Main {
    public static void main(String[] args) {
        int i = 10;
        Fibonacci fibonacci = new Fibonacci();
        long fib = fibonacci.getFibonacci(i);
        int maxDigit = fibonacci.getMaxDigit(fib);
        System.out.printf("f(%d) = %d  # вернет [(%d, %d)]%n", i, fib, maxDigit, fibonacci.getCountOfMaxDigit(fib, maxDigit));
    }
}