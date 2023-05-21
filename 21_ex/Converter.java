public class Converter {
    private final String number;

    public Converter(String number) {
        this.number = number;
    }
    public String convert() {
        StringBuilder newNumber = new StringBuilder();
        for (int i = 0; i < number.length(); i++) {
            switch (number.charAt(i)) {
                case '0' -> newNumber.append('0');
                case '1' -> newNumber.append('7');
                case '2' -> newNumber.append('8');
                case '3' -> newNumber.append('9');
                case '4' -> newNumber.append('4');
                case '5' -> newNumber.append('5');
                case '6' -> newNumber.append('6');
                case '7' -> newNumber.append('1');
                case '8' -> newNumber.append('2');
                case '9' -> newNumber.append('3');
            }
        }
        return newNumber.toString();
    }
}
