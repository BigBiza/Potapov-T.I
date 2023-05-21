public class Func {
    public int result(int number) {
        if (number==0) {
            return 0;
        } else if (number==1) {
            return 1;
        } else if (number%2==0) {
            return result(number / 2);
        } else {
            return result(number / 2) + result(number / 2 + 1);
        }
    }
}
