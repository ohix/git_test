//ZweiHochApp

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class ZweiHochApp_Swing extends JFrame {

  JLabel label_n;
  JTextField text_n, text_erg;
  JButton b;

  public ZweiHochApp_Swing() {
    setLayout(new FlowLayout());
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setTitle("2 hoch n");
    setLocation(50,50);
    setSize(350,70);

    label_n = new JLabel("n=");
    add(label_n);
    text_n = new JTextField(5);
    add(text_n);
    b = new JButton("2 hoch n");
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
    int n=1;
    try {n = Integer.parseInt(text_n.getText());
        if (n>=0) {int erg = zweihoch(n);
                  text_erg.setText(String.valueOf(erg));
        }  
    }catch (NumberFormatException err) {text_erg.setText("Error");}
  }
}

  int zweihoch(int n){
    if (n==0) {return 1;} else {return zweihoch(n-1)*2;}
  }

  public static void main(String[] args) {
    (new ZweiHochApp_Swing()).setVisible(true);
  }

}