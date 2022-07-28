/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Main;

import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class Utiles {

  public static int leerInt(String msg) {
    String entrada = JOptionPane.showInputDialog(msg);
    return Integer.parseInt(entrada);
  }

  public static double leerDouble(String msg) {
    String entrada = JOptionPane.showInputDialog(msg);
    return Double.parseDouble(entrada);
  }
}
