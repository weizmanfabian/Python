/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Main;

import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class Main {

  /**
   * @param args the command line arguments
   */
  public void testOficina() {
    Oficina oficina = new Oficina();
    oficina.setMarca();
    oficina.setReferencia();
    oficina.setObjCPU();
    oficina.setRam();
    oficina.setCapacidadDiscoDuro();
    oficina.setValor();
    JOptionPane.showConfirmDialog(null, oficina);
  }

  public void testProgramador() {
    Programador pg = new Programador();
    pg.setMarca();
    pg.setReferencia();
    pg.setObjCPU();
    pg.setRam();
    pg.setCapacidadDiscoDuro();
    pg.setCapacidadSDD();
    pg.setValor();
    JOptionPane.showConfirmDialog(null, pg);
  }

  public void testGamer() {
    Gamer gm = new Gamer();
    gm.setMarca();
    gm.setReferencia();
    gm.setObjCPU();
    gm.setRam();
    gm.setCapacidadDiscoDuro();
    gm.setCapacidadSDD();
    gm.setObGPU();
    gm.setValor();
    JOptionPane.showConfirmDialog(null, gm);
  }

  public static void main(String[] args) {
    // TODO code application logic here
    Main test = new Main();
    // test.testOficina();
    // test.testProgramador();
    test.testGamer();

  }

}
