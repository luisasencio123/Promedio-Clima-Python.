# ============================================
# Programa: Promedio semanal del clima
# Paradigma: Programación Tradicional
# Lenguaje: Python
# ============================================

def ingresar_temperaturas():
    """
    Función que solicita al usuario ingresar
    las temperaturas de los 7 días de la semana.
    Retorna una lista con las temperaturas.
    """
    temperaturas = []

    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal
    a partir de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal que organiza
    la ejecución del programa.
    """
    print("=== PROMEDIO SEMANAL DEL CLIMA (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
