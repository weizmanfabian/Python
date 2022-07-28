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
public abstract class Computador {

  private CPU objCPU;
  protected int valor;
  private String marca;
  private String referencia;

  public Computador() {
    objCPU = new CPU();
    this.valor = 0;
    this.marca = this.referencia = "";
  }

  public CPU getObjCPU() {
    return objCPU;
  }

  public void setObjCPU() {
    // this.objCPU = objCPU;
    this.objCPU.setMarca();
    this.objCPU.setVelocidad();
    this.objCPU.setCantNucleos();
  }

  public int getValor() {
    return valor;
  }

  // public void setValor(int valor) {
  // this.valor = valor;
  // }

  // obliga a todas las clases hijas a implementarlos = polimorfismo
  public abstract void setValor();

  public String getMarca() {
    return marca;
  }

  public void setMarca() {
    // this.marca = marca;
    this.marca = JOptionPane.showInputDialog("Ingrese la marca del PC:");
  }

  public String getReferencia() {
    return referencia;
  }

  public void setReferencia() {
    // this.referencia = referencia;
    this.referencia = JOptionPane.showInputDialog("Ingrese la referencia del PC:");
  }

  public String toString() {
    return "Info de PC\nMarca = " + this.marca + "\nReferencia = " + this.referencia + "\n" + objCPU.toString();
  }

}
