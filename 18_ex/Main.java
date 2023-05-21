public class Main {
    public static void main(String[] args) {
        List list = new List(10);
        System.out.println(list);
        System.out.println(list.findMax());
        list.getLeftList();
        list.getRightList();
    }
}
