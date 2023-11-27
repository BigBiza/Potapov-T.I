import java.util.ArrayList;

public class CompareGroup implements java.io.Serializable {
    private ArrayList<Student> products = new ArrayList<>();
    public void add(Students product_service) {
        this.products.add(product_service);
    }
    public ArrayList<Student> getProducts() {
        return products;
    }
    public void setProducts(ArrayList<Student> products) {
        this.products = products;
    }
    public String show() {
        StringBuilder s = new StringBuilder();
        for (Student product : this.products) {
            s.append(product).append("\n");
        }
        return s.toString();
    }
}
