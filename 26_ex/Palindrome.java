public class Palindrome {
    private final String line;
    public Palindrome(String line) {
        this.line = line;
    }

    public int check() {
        StringBuilder newWord = new StringBuilder();
        int length = line.length();
        if (length % 2 == 0) {
            for (int i = 0; i < length / 2; i++) {
                if (line.charAt(i) == line.charAt(length - 1 - i)) {
                    newWord.append(line.charAt(i));
                } else {
                    newWord = new StringBuilder();
                }
            }
        } else {
            for (int i = 0; i < length / 2 + 1; i++) {
                if (line.charAt(i) == line.charAt(length - 1 - i)) {
                    newWord.append(line.charAt(i));
                } else {
                    newWord = new StringBuilder();
                }
            }
        }
        if (length % 2 == 0) {
            return newWord.length() * 2;
        } else {
            return newWord.length() * 2 - 1;
        }
    }
}
