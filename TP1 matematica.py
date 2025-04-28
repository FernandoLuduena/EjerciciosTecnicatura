from time import sleep

# --- Primer bucle: Conversión manual a binario ---
print("--- Conversión manual a binario ---")
for i in range(16):
    decimal = i
    binario = ''

    # Caso especial para el número 0.
    if decimal == 0:
        binario = '0'
    else:
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal //= 2

    print(f"El número {i} en binario es: {binario}")
    # Pausa de 0.5 segundos para visualizar la salida paso a paso.
    sleep(0.5)

# --- Segundo bucle: Conversión a binario usando la función incorporada bin() ---
print("\n--- Conversión usando la función bin() ---")
for numero in range(16):
    # La función bin() convierte un entero a una cadena binaria con el prefijo '0b'.
    # Usamos [2:] para eliminar el prefijo '0b' y obtener solo la representación binaria.
    print(f"{numero} en binario es {bin(numero)[2:]}")
    sleep(0.5)