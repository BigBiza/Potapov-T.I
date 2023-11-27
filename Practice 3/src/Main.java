public class Main implements java.io.Serializable {
    public static void main(String[] args) {
        CompareGroup compareGroup = new CompareGroup();
        new Thread(() -> new MainStudentFrame(compareGroup).setVisible(true)).start();
    }
}
