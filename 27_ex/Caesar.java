public class Caesar {
    String word;
    int number;
    String direction;
    public Caesar(String word, int number, String direction) {
        this.word = word;
        this.number = number;
        this.direction = direction;
    }
    public StringBuilder cipher() {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (Character.isLetter(c)) {
                if (direction.equals("right")) {
                    c = (char) ((c - 'a' + number) % 26 + 'a');
                } else if (direction.equals("left")) {
                    c = (char) ((c - 'a' - number + 26) % 26 + 'a');
                }
            }
            result.append(c);
        }
        return result;
    }
}
