import javax.swing.*;

public class AddStudentFrame extends JFrame {
    private JPanel mainProductPanel;
    private JTextField textFieldName;
    private JTextField textFieldGroup;
    private JButton backButton;
    private JButton okButton;
    private CompareGroup compareGroup;

    public AddStudentFrame(CompareGroup comparProduct) {
        this.setContentPane(mainProductPanel);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(1000, 1000);
        this.setTitle("Добавление студента");
        this.compareGroup = comparProduct;
        backButton.addActionListener(e -> {
            AddStudentFrame.this.setVisible(false);
            new MainStudentFrame(compareGroup).setVisible(true);
        });
        okButton.addActionListener(e -> {
            try {
                compareGroup.add(new Students(textFieldName.getText(),
                        Integer.parseInt(textFieldGroup.getText())));
            } catch (NumberFormatException ignored) {}
            AddStudentFrame.this.setVisible(false);
            new MainStudentFrame(compareGroup).setVisible(true);
        });
    }
}
