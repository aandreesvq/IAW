# EJERCICIO 1 
numero = int(input("Por favor, ingresa un número: "))
if numero == 1000:
    print("¡Ganaste un premio!")

# EJERCICIO 2
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
if numero1 < numero2:
    print("El primer número es menor:", numero1)
else:
    print("El segundo número es menor:", numero2)

# EJERCICIO 3
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
if numero1 < numero2:
    print("El primer número es menor:", numero1)
elif numero2 < numero1:
    print("El segundo número es menor:", numero2)
else:
    print("Ambos números son iguales.")

# EJERCICIO 4
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
numero3 = float(input("Por favor, ingresa el tercer número: "))
if numero1 >= numero2 and numero1 >= numero3:
    print("El primer número es el mayor:", numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("El segundo número es el mayor:", numero2)
else:
    print("El tercer número es el mayor:", numero3)

# EJERCICIO 5
diasemana = input("Por favor, ingresa un dia de la semana en minúsculas: ")
if diasemana == "lunes":
    print("Comienza la semana")
elif diasemana == "viernes":
    print("Ya es viernes")
elif diasemana == "sábado" or diasemana == "domingo":
    print("Es fin de semana")
else:
    print("Ese día no es lunes, viernes, sábado ni domingo.")

# EJERCICIO 6
numero = int(input("Por favor, ingresa un número entero: "))
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

# EJERCICIO 7
edad = int(input("Por favor, ingresa tu edad: "))
ingresos_mensuales = float(input("Por favor, ingresa tus ingresos mensuales en euros: "))
if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes tributar.")
else:
    print("No necesitas tributar.")
