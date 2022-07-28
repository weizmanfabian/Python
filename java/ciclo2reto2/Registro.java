
package java.ciclo2reto2;

import java.util.ArrayList;
import java.util.Scanner;

public class Registro {

  public static void main(String[] args) {
    Registro registro = new Registro();
    registro.procesarComandos();
  }

  ArrayList estudiantes = new ArrayList();
  Scanner scannerInt = new Scanner(System.in);
  Scanner scannerString = new Scanner(System.in);

  public void agregarEstudiante(String[] newObj) {
    if ("Pregrado".equals(newObj[1])) {
      Pregrado pregrado = new Pregrado(newObj[2], newObj[3] + " anios", newObj[4], newObj[5],
          Integer.parseInt(newObj[6]));
      estudiantes.add(pregrado);
    } else if ("Posgrado".equals(newObj[1])) {
      Posgrado posgrado = new Posgrado(newObj[2], newObj[3] + " anios", newObj[4], newObj[5], newObj[6]);
      estudiantes.add(posgrado);
    }
  }

  public void listarEstudiantes() {
    System.out.println("***Listado de estudiantes***");
    for (Object estudiante : estudiantes) {
      System.out.println(estudiante);
    }
  }

  public void procesarComandos() {
    String opcion;
    // System.out.println("Agregar Objeto Estudiante. Pegue el objeto\n2 => Listar
    // Estudiantes\n3 => Salir");
    opcion = scannerInt.nextLine();
    String[] newOpcion = opcion.split("&");
    switch (Integer.parseInt(newOpcion[0])) {
      case 1:
        agregarEstudiante(newOpcion);
        procesarComandos();
        break;
      case 2:
        listarEstudiantes();
        procesarComandos();
        break;
      case 3:
        // System.out.println("Genial, usaste un maravilloso programa.\nSee you later");
        break;
      default:
        System.out.println("Opción inválida");
        procesarComandos();
        break;
    }
  }

}
