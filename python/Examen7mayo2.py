# Ejercicio 1
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    if x == 1 or x == 2:
        print(x)

# Ejercicio 2 
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
numero_mes = int(input("Ingrese el número de mes (1-12): "))
if 1 <= numero_mes <= 12:
    nombre_mes = meses[numero_mes - 1]
    cantidad_dias = dias_por_mes[numero_mes - 1]
    print(f"El mes número {numero_mes} es {nombre_mes} y tiene {cantidad_dias} días.")
else:
    print("Número de mes inválido. Por favor, ingrese un número entre 1 y 12.")

# Ejercicio 3
notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
print("Notas obtenidas:")
for nota in notas:
    print(nota)
media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota media: {media}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

# Ejercicio 4
num_alumnos = int(input("Ingrese el número de alumnos: "))
notas_por_alumno = {}
for i in range(1, num_alumnos + 1):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i}: ")
    notas_alumno = []
    while True:
        nota = float(input(f"Ingrese la nota del alumno {i} (introduzca un número negativo para terminar): "))
        if nota < 0:
            break
        notas_alumno.append(nota)
    media_alumno = sum(notas_alumno) / len(notas_alumno) if notas_alumno else 0
    notas_por_alumno[nombre_alumno] = {'notas': notas_alumno, 'media': media_alumno}
print("\nLista de alumnos y su nota media:")
for nombre, datos in notas_por_alumno.items():
    print(f"Alumno: {nombre}, Notas: {datos['notas']}, Nota Media: {datos['media']}")
