/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Main;

/**
 *
 * @author User
 */
public class Oficina extends Computador {

  private int ram;
  private int capacidadDiscoDuro;

  public Oficina() {
    super();
    this.ram = this.capacidadDiscoDuro = 0;
  }

  public void setRam() {
    this.ram = Utiles.leerInt("Ingrese la RAM");
  }

  public void setCapacidadDiscoDuro() {
    this.capacidadDiscoDuro = Utiles.leerInt("Ingrese la capacidad del disco duro (DD).");
  }

  public int getRam() {
    return ram;
  }

  public int getCapacidadDiscoDuro() {
    return capacidadDiscoDuro;
  }

  public String toString() {
    return super.toString() + "\nRam = " + this.ram + "\nCapacidad de disco duro = " + this.capacidadDiscoDuro
        + "\nValor = " + this.valor;
  }

  @Override
  public void setValor() {
    valor = 1000;
  }

}
