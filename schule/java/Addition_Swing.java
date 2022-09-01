import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class Addition_Swing extends JFrame {

  JLabel label_n, label_m;
  JTextField text_n, text_m, text_erg;
  JButton b;

  public Addition_Swing() {
    setLayout(new FlowLayout());
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setTitle("Additionsrechner");
    setLocation(50,50);
    setSize(350,70);

    label_n = new JLabel("n =");
    add(label_n);
    text_n = new JTextField(5);
    add(text_n);
    label_m = new JLabel("m =");
    add(label_m);
    text_m = new JTextField(5);
    add(text_m);
    b = new JButton("addieren");
    add(b);
    text_erg = new JTextField(5);
    text_erg.setEditable(false);
    add(text_erg);

    Waechter_b wb = new Waechter_b();
    b.addActionListener(wb);
 }

class Waechter_b implements ActionListener {
  
  public void actionPerformed(ActionEvent e) {
    text_erg.setText("");
    int n=0;
    int m=0;
    try {n = Integer.parseInt(text_n.getText()); m = Integer.parseInt(text_m.getText());
        int erg = addit(n,m);
        text_erg.setText(String.valueOf(erg)); 
    }catch (NumberFormatException err) {text_erg.setText("Error");}
  }
}

  int addit(int n, int m){
    // if (n==0) {return 1;} else {return zweihoch(n-1)*2;}
    return n + m;
  }

  public static void main(String[] args) {
    (new Addition_Swing()).setVisible(true);
  }
}