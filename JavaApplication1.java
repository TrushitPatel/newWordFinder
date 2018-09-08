import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.io.IOException;
import java.io.*;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class JavaApplication1 extends JPanel
   implements ActionListener {
   JButton go;

   JFileChooser chooser;
   String choosertitle;
   private JLabel headerLabel;
   
   
  public JavaApplication1() {
    go = new JButton("select subtitle file");
    go.addActionListener(this);
    add(go);
    headerLabel = new JLabel(".", JLabel.CENTER); 
    add(headerLabel);
   }

   @Override
  public void actionPerformed(ActionEvent e) {            
    chooser = new JFileChooser(); 
    chooser.setCurrentDirectory(new java.io.File("/home/sarkijatru"));
    chooser.setDialogTitle(choosertitle);
    chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);

    chooser.setAcceptAllFileFilterUsed(true);
    //    
    if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) { 
         headerLabel.setText(chooser.getSelectedFile().toString());

            System.out.println("inside:");

            Process p = Runtime.getRuntime().exec("python /home/sarkijatru/Desktop/documentry_Saturday/program/finallyDone.py");
            PrintWriter pw = new PrintWriter(p.getOutputStream(),true);
            pw.write(chooser.getSelectedFile().toString());
            System.out.println(p.waitFor());

            System.out.println("done:");
            
         headerLabel.setText("done");
      }
    else {
      System.out.println("No Selection ");
      }
    }

   @Override
  public Dimension getPreferredSize(){
    return new Dimension(500, 200);
    }

  public static void main(String s[]) {
    JFrame frame = new JFrame("color-i-fy");
    JavaApplication1 panel = new JavaApplication1();
    frame.addWindowListener(
      new WindowAdapter() {
        @Override
        public void windowClosing(WindowEvent e) {
          System.exit(0);
          }
        }
      );
    frame.getContentPane().add(panel,"Center");
    frame.setSize(panel.getPreferredSize());
    frame.setVisible(true);
    }
}