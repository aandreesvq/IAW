# EJERCICIO 1
diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': 'Y'}
divisa = input("Por favor, ingresa una divisa: ")
if divisa in diccionario_divisas:
    print("El símbolo de", divisa, "es:", diccionario_divisas[divisa])
else:
    print("La divisa ingresada no está en el diccionario.")

# EJERCICIO 2
nombre = input("Por favor, ingresa tu nombre: ")
edad = input("Por favor, ingresa tu edad: ")
direccion = input("Por favor, ingresa tu dirección: ")
telefono = input("Por favor, ingresa tu número de teléfono: ")
informacion_usuario = {'nombre': nombre, 'edad': edad, 'dirección': direccion, 'teléfono': telefono}
print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['dirección']} y su número de teléfono es {informacion_usuario['teléfono']}.")

# EJERCICIO 3
precios_frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input("Por favor, ingresa una fruta: ")
kilos = float(input("Por favor, ingresa el número de kilos: "))
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total} euros.")
else:
    print("La fruta ingresada no está en el diccionario.")

# EJERCICIO 4
meses = {
    '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo',
    '06': 'junio', '07': 'julio', '08': 'agosto', '09': 'septiembre', '10': 'octubre',
    '11': 'noviembre', '12': 'diciembre'
}
fecha = input("Por favor, ingresa una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split('/')
nombre_mes = meses[mes]
print(f"La fecha es: {dia} de {nombre_mes} de {anio}")

# EJERCICIO 5
creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")
    total_creditos += creditos
print("El número total de créditos del curso es:", total_creditos)

# EJERCICIO 6
informacion_persona = {}
while True:
    clave = input("Por favor, ingresa el tipo de información (nombre, edad, sexo, teléfono, correo electrónico, etc.): ")
    valor = input("Por favor, ingresa el valor de esa información: ")
    informacion_persona[clave] = valor
    print("Información actualizada:", informacion_persona)
    continuar = input("¿Deseas agregar más información? (si/no): ")
    if continuar.lower() != 'si':
        break

# EJERCICIO 7 
cesta_compra = {}
while True:
    articulo = input("Por favor, ingresa un artículo: ")
    precio = float(input("Por favor, ingresa el precio del artículo: "))
    cesta_compra[articulo] = precio
    continuar = input("¿Deseas agregar otro artículo? (si/no): ")
    if continuar.lower() != 'si':
        break
print("Lista de la compra:")
total = 0
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: {precio}€")
    total += precio
print("Total:", total, "€")

# EJERCICIO 8
palabras_traducciones = input("Por favor, ingresa las palabras y sus traducciones en formato palabra:traducción separadas por comas: ")
parejas = palabras_traducciones.split(',')
diccionario_traduccion = {}
for pareja in parejas:
    palabra, traduccion = pareja.split(':')
    diccionario_traduccion[palabra.strip()] = traduccion.strip()
frase_espanol = input("Por favor, ingresa una frase en español: ")
palabras_frase = frase_espanol.split()
frase_traducida = " ".join(diccionario_traduccion.get(palabra, palabra) for palabra in palabras_frase)
print("La frase traducida al inglés es:", frase_traducida)

# EJERCICIO 9
facturas = {}
cantidad_cobrada = 0
cantidad_pendiente = 0
while True:
    print("\nOpciones:")
    print("1. Añadir una nueva factura")
    print("2. Pagar una factura existente")
    print("3. Terminar")
    opcion = input("Por favor, selecciona una opción (1, 2 o 3): ")
    if opcion == '1':
        numero_factura = input("Por favor, ingresa el número de factura: ")
        coste_factura = float(input("Por favor, ingresa el coste de la factura: "))
        facturas[numero_factura] = coste_factura
        cantidad_pendiente += coste_factura
        print("Factura añadida correctamente.")
    elif opcion == '2':
        numero_factura = input("Por favor, ingresa el número de factura a pagar: ")
        if numero_factura in facturas:
            cantidad_cobrada += facturas[numero_factura]
            cantidad_pendiente -= facturas[numero_factura]
            del facturas[numero_factura]
            print("Factura pagada correctamente.")
        else:
            print("La factura ingresada no existe.")
    elif opcion == '3':
        break
    else:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
    print("Cantidad cobrada hasta el momento:", cantidad_cobrada)
    print("Cantidad pendiente de cobro:", cantidad_pendiente)

# EJERCICIO 10
def agregar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    preferente = input("¿Es un cliente preferente? (si/no): ").lower() == 'si'
    base_datos[nif] = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'correo': correo, 'preferente': preferente}
    print("Cliente añadido correctamente.")
def eliminar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente a eliminar: ")
    if nif in base_datos:
        del base_datos[nif]
        print("Cliente eliminado correctamente.")
    else:
        print("El cliente no está en la base de datos.")
def mostrar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente a mostrar: ")
    if nif in base_datos:
        cliente = base_datos[nif]
        print("Datos del cliente:")
        print("NIF:", nif)
        for clave, valor in cliente.items():
            print(clave.capitalize() + ":", valor)
    else:
        print("El cliente no está en la base de datos.")
def listar_clientes(base_datos):
    print("Lista de todos los clientes:")
    for nif, cliente in base_datos.items():
        print("NIF:", nif, "- Nombre:", cliente['nombre'])
def listar_clientes_preferentes(base_datos):
    print("Lista de clientes preferentes:")
    for nif, cliente in base_datos.items():
        if cliente['preferente']:
            print("NIF:", nif, "- Nombre:", cliente['nombre'])
clientes = {}
while True:
    print("\nMenú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Por favor, ingrese una opción: ")

    if opcion == '1':
        agregar_cliente(clientes)
    elif opcion == '2':
        eliminar_cliente(clientes)
    elif opcion == '3':
        mostrar_cliente(clientes)
    elif opcion == '4':
        listar_clientes(clientes)
    elif opcion == '5':
        listar_clientes_preferentes(clientes)
    elif opcion == '6':
        print("Programa terminado.")
        break
    else:
        print("Opción inválida.")
