from tkinter.constants import SEL_FIRST


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        print(n)
        return n*factorial(n-1)

 def menu():
     opcion=0
     while True:
         print("===Menu===")
         print("1. Factorial")
         print("2. Suma de primeros numeros")
         print("3. Calcular el fibonacci")
         print("4. Contar letras")
         print("5. Invertir una cadena de texto")
         print("6. Calcular potencia")
         print("7. Salir")
         opcion=int(input("Selecciona una opcion"))
         if opcion==1:
             n=int(input("Ingrese un numero entero que desee saber su factorial: "))
             print(factorial(n))
         elif opcion==2:
