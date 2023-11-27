import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;

public class MainStudentFrame extends JFrame {
    private JPanel mainProductPanel;
    private JButton showGroups;
    private JButton studentButton;

    public MainStudentFrame(CompareGroup compareGroup) {
        this.setContentPane(mainProductPanel);
        this.setTitle("Практическая работа");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.pack();
        showGroups.addActionListener(e -> {
            new ShowStudentFrame(compareGroup).setVisible(true);
            MainStudentFrame.this.setVisible(false);
        });
        studentButton.addActionListener(e -> {
            new AddStudentFrame(compareGroup).setVisible(true);
            MainStudentFrame.this.setVisible(false);
        });
    }

    public static void Saving(CompareGroup compareGroup) {
        try{
            FileWriter writer = new FileWriter("test.txt");
            writer.write(compareGroup.show());
            writer.close();
            System.out.println("Данные обновлены");
        } catch (IOException e) {
            System.out.println("Ошибка");
            e.printStackTrace();
        }
    }

    public static CompareGroup LoadingByte(CompareGroup compareGroup) {
        ObjectInputStream in;
        try {
            in = new ObjectInputStream(new BufferedInputStream(
                    new FileInputStream("text.txt")
            ));
            try {
                compareGroup.setProducts((ArrayList<Student>)in.readObject());
            } catch (IOException e) {
                System.out.println("Maybe disk is full, or you haven't permissions to write");
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            try {
                in.close();
            } catch (FileNotFoundException e) {
                System.out.println("Ошибка");
            }
        } catch (FileNotFoundException e) {
            System.out.println("Отсутсвует файл");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return compareGroup;
    }

    public static void SavingByte(CompareGroup comparProduct) {
        ObjectOutputStream out;
        try {
            out = new ObjectOutputStream(new BufferedOutputStream(
                    new FileOutputStream("text.txt")
            ));
            try {
                out.writeObject(comparProduct.getProducts());
            } catch (IOException e) {
                System.out.println("Maybe disk is full, or you haven't permissions to write");
            }
            try {
                out.close();
            } catch (IOException e) {
                System.out.println("Ошибка");
            }
        } catch (FileNotFoundException e) {
            System.out.println("Отсутствует файл");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
