/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ciclo2reto3;

import java.util.ArrayList;
import java.util.List;
import javax.xml.validation.Validator;

/**
 *
 * @author User
 */
public class Obra {

  public List<Integer> clases(List<Integer> lista) {
    List<Integer> output = new ArrayList<>();
    for (int i : lista) {
      if (!output.contains(i)) {
        output.add(i);
      }
    }
    // System.out.println(output);
    return output;
  }

  public List<Integer> meFaltanDeLaClase(List<Integer> obrasQueFaltan, List<Integer> categorias, int numero) {
    ArrayList<Integer> output = new ArrayList<>();
    ArrayList<Integer> val = new ArrayList<>();
    for (int i = 0; i < categorias.size(); i++) {
      if (numero == categorias.get(i)) {
        val.add(i);
      }
    }
    for (Integer o : obrasQueFaltan) {
      if (val.contains(o)) {
        output.add(o);
      }
    }
    // System.out.println(output);
    return output;
  }

  public List<Integer> noTengo(List<Integer> listaMuseoA, List<Integer> listaMuseoB) {
    List<Integer> output = new ArrayList<>();
    for (Integer musA : listaMuseoA) {
      if (!listaMuseoB.contains(musA)) {
        output.add(musA);
      }
    }
    // System.out.println(output);
    return output;
  }

  public Integer puedoCambiar(List<Integer> listDuplicMusA, List<Integer> listDuplicMusB) {
    Integer contador = 0;
    if (listDuplicMusA.size() > listDuplicMusB.size()) {
      for (Integer b : listDuplicMusB) {
        if (!listDuplicMusA.contains(b)) {
          contador++;
        }
      }
    } else {
      for (Integer a : listDuplicMusA) {
        if (!listDuplicMusB.contains(a)) {
          contador++;
        }
      }
    }
    // System.out.println(contador);
    return contador;
  }

}
