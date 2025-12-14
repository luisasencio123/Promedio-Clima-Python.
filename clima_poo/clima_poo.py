# ============================================
# Programa: Promedio semanal del clima
# Paradigma: Programación Orientada a Objetos
# Lenguaje: Python
# ============================================

class Clima:
    """
    Clase que representa la información
    del clima semanal.
    """

    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas
        de los 7 días de la semana.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal
        de las temperaturas ingresadas.
        """
        if len(self.__temperaturas) == 0:
            return 0

        return sum(self.__temperaturas) / len(self.__temperaturas)


def main():
    """
    Función principal que crea un objeto
    de la clase Clima y utiliza sus métodos.
    """
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

