public class Main {
    public static void main(String[] args) {
        String text = "Пупе и Лупе поручили построить памятник около здания администрации города. Внезапно Лупу отправили в длительную командировку, поэтому Пупе пришлось строить за Лупу в центре города.";
        String[] sentences = text.split("\\.\\s*");

        for (int i = 0; i < sentences.length; i++) {
            String[] words = sentences[i].split("\\s+");
            for (int j = 0; j < words.length; j++) {
                char firstLetter = words[j].charAt(0);
                String rest = words[j].substring(1);
                words[j] = rest + firstLetter + "ауч";
            }
            sentences[i] = String.join(" ", words) + ".";
        }

        String result = String.join(" ", sentences);
        System.out.println(result);
    }
}