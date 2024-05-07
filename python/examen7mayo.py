# Ejercicio 1
for i in range(10, -1, -1):
    print(i)

# Ejercicio 2
numeros = []
while True:
    numero = input("Por favor, ingresa un número (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    numeros.append(int(numero))
numero_buscar = int(input("Por favor, ingresa un número para buscar en la lista: "))
apariciones = numeros.count(numero_buscar)
print(f"El número {numero_buscar} aparece {apariciones} veces en la lista.")

# Ejercicio 3
caracter = input("Por favor, ingresa un carácter: ")
if caracter.lower() in 'aeiou':
    print(f"El carácter '{caracter}' sí es una vocal.")
else:
    print(f"El carácter '{caracter}' no es una vocal.")

# Ejercicio 4
lista1 = [6, 5, 8, 4, 3]
lista2 = [2, 9, 2, 1]
conjunto1 = set(lista1)
conjunto2 = set(lista2)
if conjunto1.intersection(conjunto2):
    print("Sí existen elementos repetidos en ambas listas.")
else:
    print("No existen elementos repetidos en ambas listas.")

# Ejercicio 5
adivina_numero = 42
intentos = 0
while True:
    intento = int(input("Intenta adivinar el número (1-100): "))
    intentos += 1
    if intento == adivina_numero:
        print(f"¡Has acertado el número! Te ha llevado {intentos} intentos.")
        break
    elif intento < adivina_numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")
