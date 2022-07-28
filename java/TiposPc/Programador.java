/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Main;

/**
 *
 * @author User
 */
public class Programador extends Oficina {

  private int capacidadSDD;

  public Programador() {
    super();
    this.capacidadSDD = 0;
  }

  public void setCapacidadSDD() {
    this.capacidadSDD = Utiles.leerInt("Ingrese la capacidad del SDD:");
  }

  public void setValor() {
    super.setValor();
    valor += 350;
  }

  public int getCapacidadSDD() {
    return capacidadSDD;
  }

  public String toString() {
    return super.toString() + "\nCapacidad de SDD = " + this.capacidadSDD;
  }
}
