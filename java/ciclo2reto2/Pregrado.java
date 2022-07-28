package java.ciclo2reto2;

public class Pregrado extends Estudiante {

  private int cantidad_creditos;

  public Pregrado(String nombre, String edad, String programa, String tipo_etnia, int cantidad_creditos) {
    super(nombre, edad, programa, tipo_etnia);
    this.cantidad_creditos = cantidad_creditos;
  }

  public int getCantidad_creditos() {
    return cantidad_creditos;
  }

  public void setCantidad_creditos(int cantidad_creditos) {
    this.cantidad_creditos = cantidad_creditos;
  }

  @Override
  public String toString() {
    return "\tEstudiante Pregrado" + super.toString() + "\n\tCreditos aprobados: " + cantidad_creditos;
  }

}
