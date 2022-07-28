package java.ciclo2reto2;

public class Estudiante {

    private String nombre;
    private String edad;
    private String programa;
    private String tipo_etnia;

    public Estudiante(String nombre, String edad, String programa, String tipo_etnia) {
        this.nombre = nombre;
        this.edad = edad;
        this.programa = programa;
        this.tipo_etnia = tipo_etnia;
    }

    public Estudiante() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPrograma() {
        return programa;
    }

    public void setPrograma(String programa) {
        this.programa = programa;
    }

    public String getTipo_etnia() {
        return tipo_etnia;
    }

    public void setTipo_etnia(String tipo_etnia) {
        this.tipo_etnia = tipo_etnia;
    }

    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "\n\tNombre: " + nombre
                + "\n\tEdad: " + edad
                + "\n\tPrograma: " + programa + "\n\tEtnia: " + tipo_etnia;
    }

}
