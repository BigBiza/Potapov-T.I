import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ShowStudentFrame extends JFrame {
    private JPanel mainStudentPanel;
    private JButton okStudentButton;
    private JTextArea showTextProductArea;
    private CompareGroup product;

    public ShowStudentFrame(CompareGroup compareGroup) {
        this.setContentPane(mainStudentPanel);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(1000, 1000);
        this.setTitle("Коллекция");
        showTextProductArea.setEditable(false);
        showTextProductArea.setText(compareGroup.show());
        okStudentButton.addActionListener(e -> {
            ShowStudentFrame.this.setVisible(false);
            new MainStudentFrame(compareGroup).setVisible(true);
        });
    }
}
