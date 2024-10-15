from src.logica.OperacionesEnteros import OperacionesEnteros

if __name__ == '__main__':
    cantidadNumeros = int(input("Cantidad de números: "))
    numeros = []

    for i in range(cantidadNumeros):
        while True:
            try:
                print(f"Número {i+1:2}: ", end="", flush=True)
                numero = int(input(""))  # Intentar convertir la entrada a entero
                numeros.append(numero)
                break  # Si todo está bien, salir del bucle
            except ValueError:
                print("Error: Debes ingresar un número entero válido. Inténtalo de nuevo.")

    print(f"Números = {numeros}")
    operacionesEnteros = OperacionesEnteros(numeros)
    try:
        print(f"MCM= {operacionesEnteros.calcularMCM()}")
    except Exception as e:
        print(f"Error al calcular el MCM: {e}")
