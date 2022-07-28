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
public class GPU {

  private String marca;
  private double memoria;

  public GPU() {
    this.marca = "";
    this.memoria = 0.0;
  }

  public String getMarca() {
    return marca;
  }

  public void setMarca() {
    this.marca = JOptionPane.showInputDialog("Ingrese la marca de la GPU:");
  }

  public double getMemoria() {
    return memoria;
  }

  public void setMemoria() {
    this.memoria = Utiles.leerDouble("Ingrese la memoria de la GPU:");
  }

  public String toString() {
    return "Info GPU\nMarca = " + this.marca + "\nMemoria = " + this.memoria;
  }

}
