def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

def Suma(n):
    if n == 0:
        return 0
    else:
        return n + Suma(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def Contar_Letras(palabra, letra):
    if palabra == "":
        return 0
    if palabra[0] == letra:
        return 1 + Contar_Letras(palabra[1:], letra)
    else:
        return Contar_Letras(palabra[1:], letra)

def InvertirCadena(cadena):
    if cadena == "":
        return ""
    else:
        return InvertirCadena(cadena[1:]) + cadena[0]

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def menu():
    while True:
        print("\n=== Menú ===")
        print("1. Calcular el factorial de un número")
        print("2. Suma de los primeros N números naturales")
        print("3. Calcular el n-ésimo número de Fibonacci")
        print("4. Contar cuántas veces aparece una letra en una palabra")
        print("5. Invertir una cadena de texto")
        print("6. Calcular la potencia de un número (base^exponente)")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-7): "))
        except ValueError:
            print(" Entrada inválida. Ingrese un número del 1 al 7.")
            continue

        if opcion == 1:
            while True:
                print("\n--- Factorial ---")
                try:
                    n = int(input("Ingrese un número entero positivo: "))
                    if n < 0:
                        print("El número debe ser positivo.")
                    else:
                        print(f"Resultado: {factorial(n)}")
                except ValueError:
                    print("Entrada inválida. Ingrese un número entero.")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 2:
            while True:
                print("\n--- Suma ---")
                try:
                    n = int(input("Ingrese un número entero positivo: "))
                    if n < 0:
                        print(" El número debe ser positivo.")
                    else:
                        print(f"Resultado: {Suma(n)}")
                except ValueError:
                    print("Entrada inválida. Ingrese un número entero.")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 3:
            while True:
                print("\n--- Fibonacci ---")
                try:
                    n = int(input("Ingrese la posición (entero positivo): "))
                    if n < 0:
                        print("El número debe ser positivo.")
                    else:
                        print(f"Fibonacci({n}) = {fibonacci(n)}")
                except ValueError:
                    print(" Entrada inválida. Ingrese un número entero.")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 4:
            while True:
                print("\n--- Contar letras ---")
                palabra = input("Ingrese una palabra: ")
                letra = input("Ingrese la letra que desea contar: ")
                if len(letra) != 1:
                    print(" Debe ingresar solo una letra.")
                else:
                    print(f"La letra '{letra}' aparece {Contar_Letras(palabra, letra)} veces.")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 5:
            while True:
                print("\n--- Invertir texto ---")
                cadena = input("Ingrese una cadena de texto: ")
                print(f"Cadena invertida: {InvertirCadena(cadena)}")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 6:
            while True:
                print("\n--- Potencia ---")
                try:
                    base = int(input("Ingrese la base: "))
                    exponente = int(input("Ingrese el exponente (entero positivo): "))
                    if exponente < 0:
                        print(" El exponente debe ser un número positivo.")
                    else:
                        print(f"{base}^{exponente} = {potencia(base, exponente)}")
                except ValueError:
                    print("Entrada inválida. Ingrese valores enteros.")
                if input("¿Desea repetir esta opción? (s/n): ").lower() != 's':
                    break

        elif opcion == 7:
            print(" Saliendo del programa... ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Ingrese un número del 1 al 7.")


menu()
