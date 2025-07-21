
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        print(n)
        return n*factorial(n-1)
def Suma(n):
    if n==0:
        return 0
    else:
        return n+Suma(n-1)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def Contar_Letras(palabra,letra):
    if palabra=="":
        return 0
    if palabra[0]==letra:
        return 1+Contar_Letras(palabra[1:], letra)
    else:
        return Contar_Letras(palabra[1:],letra)

def InvertirCadena(cadena):
    if cadena=="":
        return ""
    else:
        return InvertirCadena(cadena[1:])+cadena[0]


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
             print("Factorial")
             n=int(input("Ingrese un numero entero que desee saber su factorial: "))
             print(factorial(n))
         elif opcion==2:
             print("Suma de numeros de 1 hasta n")
             n=int(input("Ingrese el numero que desea sumar"))
             print(Suma(n))
         elif opcion==3:
             print("Fibonacci")
             n=int(input("Ingrese la posicion de la secuencia fibonacci"))
             resultado=fibonacci(n)
             print(f"Fibonacci({n})= {resultado}")
         elif opcion==4:
             print("Contar letras")
             palabra=input("Ingrese una palabra: ")
             letra=input("Ingrese la letra que desea contar: ")
             print(f"En la palabra {palabra} aparece la letra: {letra} un total de : {Contar_Letras(palabra,letra)} ")
         elif opcion==5:
             print("Invertir texto")
             cadena=input("Ingrese una cadena de texto: ")
             print(f"Cadena invertida: {InvertirCadena(cadena)}")


menu()