public class Students extends Student implements java.io.Serializable {
    public Students(){}
    public Students(String name, int group) {
        this.name = name;
        this.group = group;
    }

    @Override
    public String toString() {
        return String.format("ФИО: %s. Группа: %s", name, group);
    }
}
