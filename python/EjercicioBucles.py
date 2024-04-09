# EJERCICIO 1
palabra = input("Por favor, ingresa una palabra: ")
for _ in range(10):
    print(palabra)

# EJERCICIO 2
edad = int(input("Por favor, ingresa tu edad: "))
print("Los años que has cumplido son:")
for i in range(1, edad + 1):
    print(i)

# EJERCICIO 3
numero = int(input("Por favor, ingresa un número entero positivo: "))
if numero <= 0:
    print("El número ingresado no es positivo.")
else:
    print("Los números impares desde 1 hasta", numero, "son:")
    impares = [str(i) for i in range(1, numero + 1, 2)]
    print(", ".join(impares))

# EJERCICIO 4
numero = int(input("Por favor, ingresa un número entero positivo: "))
if numero <= 0:
    print("El número ingresado no es positivo.")
else:
    print("La cuenta atrás desde", numero, "hasta 0 es:")
    cuenta_atras = [str(i) for i in range(numero, -1, -1)]
    print(", ".join(cuenta_atras))

# EJERCICIO 5
cantidad_invertir = float(input("Por favor, ingresa la cantidad a invertir: "))
interes_anual = float(input("Por favor, ingresa el interés anual en porcentaje (por ejemplo, 5 para 5%): "))
num_anios = int(input("Por favor, ingresa el número de años de la inversión: "))
interes_anual_decimal = interes_anual / 100
for anio in range(1, num_anios + 1):
    capital_obtenido = cantidad_invertir * (1 + interes_anual_decimal) ** anio
    print("Capital obtenido en el año", anio, ":", round(capital_obtenido, 2))

# EJERCICIO 6
for i in range(1, 11):
    for j in range(1, 11):
        producto = i * j
        print(f"{i} x {j} = {producto}")
    print()

# EJERCICIO 7
contraseña = "contraseña"
intentos = 0
while True:
    intento = input("Por favor, ingresa la contraseña: ")
    if intento == contraseña:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        intentos += 1
        if intentos >= 3:
            print("Has alcanzado el máximo de intentos. Por favor, inténtalo más tarde.")
            break

# EJERCICIO 8
frase = input("Por favor, ingresa una frase: ")
letra = input("Por favor, ingresa una letra: ")
contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

# EJERCICIO 9
palabra = input("Por favor, ingresa una palabra: ")
print("Las letras de la palabra introducida, empezando por la última, son:")
for letra in reversed(palabra):
    print(letra)