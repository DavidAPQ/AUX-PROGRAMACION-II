// Clase base
class Animal {
    protected int edad;
    protected double peso;
    protected String especie;

    public Animal(int edad, double peso, String especie) {
        this.edad = edad;
        this.peso = peso;
        this.especie = especie;
    }

    // c. respirar() en la clase base
    public void respirar() {
        System.out.println(especie + " toma oxígeno del ambiente.");
    }

    // d. mover() con comportamiento general
    public void mover() {
        System.out.println(especie + " se mueve de un lugar a otro.");
    }

    // b. mostrar datos
    public void mostrarDatos() {
        System.out.println("Especie: " + especie);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Peso: " + peso + " kg");
    }
}

class Terrestre extends Animal {
    private int numeroPatas;
    private String habitat;

    public Terrestre(int edad, double peso, String especie, int numeroPatas, String habitat) {
        super(edad, peso, especie);
        this.numeroPatas = numeroPatas;
        this.habitat = habitat;
    }

    // Métodos propios
    public void caminar() {
        System.out.println(especie + " camina con sus " + numeroPatas + " patas.");
    }

    public void correr() {
        System.out.println(especie + " corre por el " + habitat + ".");
    }

    @Override
    public void respirar() {
        System.out.println(especie + " toma oxígeno del aire con sus pulmones.");
    }

    @Override
    public void mover() {
        System.out.println(especie + " se mueve caminando o corriendo sobre la tierra.");
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Número de patas: " + numeroPatas);
        System.out.println("Hábitat: " + habitat);
    }
}

class Aereo extends Animal {
    private double envergadura;
    private int alturaMaxima;

    public Aereo(int edad, double peso, String especie, double envergadura, int alturaMaxima) {
        super(edad, peso, especie);
        this.envergadura = envergadura;
        this.alturaMaxima = alturaMaxima;
    }

    // Métodos propios
    public void volar() {
        System.out.println(especie + " vuela con alas de " + envergadura + " m de envergadura.");
    }

    public void aterrizar() {
        System.out.println(especie + " aterriza después de volar hasta " + alturaMaxima + " m.");
    }

    @Override
    public void respirar() {
        System.out.println(especie + " toma oxígeno del aire con pulmones y sacos aéreos.");
    }

    @Override
    public void mover() {
        System.out.println(especie + " se mueve volando por el aire.");
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Envergadura: " + envergadura + " m");
        System.out.println("Altura máxima: " + alturaMaxima + " m");
    }
}

class Acuatico extends Animal {
    private int profundidadMaxima;
    private String tipoAgua;

    public Acuatico(int edad, double peso, String especie, int profundidadMaxima, String tipoAgua) {
        super(edad, peso, especie);
        this.profundidadMaxima = profundidadMaxima;
        this.tipoAgua = tipoAgua;
    }

    // Métodos propios
    public void nadar() {
        System.out.println(especie + " nada en agua " + tipoAgua + ".");
    }

    public void sumergirse() {
        System.out.println(especie + " se sumerge hasta " + profundidadMaxima + " m.");
    }

    @Override
    public void respirar() {
        System.out.println(especie + " toma oxígeno del agua con sus branquias.");
    }

    @Override
    public void mover() {
        System.out.println(especie + " se mueve nadando en el agua.");
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Profundidad máxima: " + profundidadMaxima + " m");
        System.out.println("Tipo de agua: " + tipoAgua);
    }
}

public class Main {
    public static void main(String[] args) {
        // b. Instanciar un objeto de cada tipo
        Terrestre perro = new Terrestre(5, 20.5, "Perro", 4, "bosque");
        Aereo aguila = new Aereo(3, 4.5, "Águila", 2.1, 3000);
        Acuatico salmon = new Acuatico(2, 6.0, "Salmón", 100, "dulce");

        // b. Mostrar datos
        System.out.println("=== Datos ===");
        perro.mostrarDatos();
        System.out.println();
        aguila.mostrarDatos();
        System.out.println();
        salmon.mostrarDatos();

        // c. respirar()
        System.out.println("\n=== Respirar ===");
        perro.respirar();
        aguila.respirar();
        salmon.respirar();

        // d. mover()
        System.out.println("\n=== Mover ===");
        perro.mover();
        aguila.mover();
        salmon.mover();

        // Métodos propios de cada clase
        System.out.println("\n=== Métodos propios ===");
        perro.caminar();
        perro.correr();
        aguila.volar();
        aguila.aterrizar();
        salmon.nadar();
        salmon.sumergirse();
    }
}