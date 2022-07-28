/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Main;

/**
 *
 * @author User
 */
public class Gamer extends Programador {
  private GPU obGPU;

  public Gamer() {
    this.obGPU = new GPU();
  }

  public GPU getObGPU() {
    return obGPU;
  }

  public void setObGPU() {
    this.obGPU.setMarca();
    this.obGPU.setMemoria();
  }

  public void setValor() {
    super.setValor();
    valor += 650;
  }

  public String toString() {
    return super.toString() + obGPU.toString();
  }

}
