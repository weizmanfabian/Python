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
public class CPU {

  private String marca;
  private double velocidad;
  private int cantNucleos;

  public CPU(String marca, double velocidad, int cantNucleos) {
    this.marca = marca;
    this.velocidad = velocidad;
    this.cantNucleos = cantNucleos;
  }

  public CPU() {
    this.marca = "";
    this.velocidad = 0.0;
    this.cantNucleos = 0;
  }

  public String getMarca() {
    return marca;
  }

  public void setMarca() {
    // this.marca = marca;
    this.marca = JOptionPane.showInputDialog("Ingrese la marca de la CPU");
  }

  public double getVelocidad() {
    return velocidad;
  }

  public void setVelocidad() {
    // this.velocidad = velocidad;
    this.velocidad = Utiles.leerDouble("Ingrese la velocidad de la CPU");
  }

  public int getCantNucleos() {
    return cantNucleos;
  }

  public void setCantNucleos() {
    // this.cantNucleos = cantNucleos;
    this.cantNucleos = Utiles.leerInt("Ingrese la cantidad de núcleos de la CPU");
  }

  @Override
  public String toString() {
    return "CPU{" + "marca=" + marca + ", \nvelocidad=" + velocidad + ", \ncantNucleos=" + cantNucleos + '}';
  }

}
