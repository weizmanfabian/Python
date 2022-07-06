/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
// package sinrepetidos;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author User
 */
public class SinRepetidos {

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) {
    //TODO code application logic here
    String text = "HOla mundo, hola yo soy el que soy, soy Weizman";
    wordRepetitions(text);
  }

  private static void wordRepetitions(String text) {
    String[] resultadoSplit = text.split(" ");
    // System.out.println(normalize(resultadoSplit[0]));
    Map<String, Integer> numWords = new HashMap<String, Integer>();
    for (String word : resultadoSplit) {
      if (!numWords.containsKey(normalize(word))) {
        // System.out.println("Si");
        numWords.put(normalize(word), 1);
      } else {
        // System.out.println("NO ");
        numWords.put(normalize(word), numWords.get(normalize(word)) + 1);
      }
    }
    System.out.println(numWords);
  }

  private static String normalize(String word) {
    // return word.toLowerCase().replaceAll("\\/[.!,¡]/g", "");
    return word.toLowerCase().replaceAll("[.!,¡]", "");
  }

}
