def procesar_numero(numero):
    while abs(numero) >= 10:  # Continuar mientras el número tenga más de un dígito
        unidades = abs(numero) % 10

        if unidades in [3, 6, 9]:
            numero = numero // 10  # Eliminar las unidades
        elif unidades in [1, 4, 7]:
            numero = (numero // 10) + 1  # Eliminar unidades y sumar 1
        elif unidades in [2, 5, 8]:
            numero = (numero // 10) - 1  # Eliminar unidades y restar 1
        else:
            break  # Si no hay más condiciones, salir del bucle

    # Verificar si el número final es divisible entre 3
    divisible = "sí" if numero % 3 == 0 else "no"
    return numero, divisible

def calcular_multiplos_y_divisibles(rango):
    divisibles = []
    multiplos = []

    for i in range(1, rango + 1):
        if i % 3 == 0:
            multiplos.append(i)  # Agregar a la lista de múltiplos

            # Comprobar si el número procesado es divisible entre 3
            procesado, es_divisible = procesar_numero(i)
            if es_divisible == "sí":
                divisibles.append(i)

    # Obtener los múltiplos de 3 que no están en la lista de divisibles
    no_en_divisibles = [num for num in multiplos if num not in divisibles]
    return divisibles, no_en_divisibles

# Ejemplo de uso
numero_inicial = int(input("Introduce un número: "))
divisibles, no_en_divisibles = calcular_multiplos_y_divisibles(numero_inicial)
print(f"Divisibles entre 3 después de procesar: {divisibles}")
print(f"Múltiplos de 3 que no están en la lista de divisibles: {no_en_divisibles}")
