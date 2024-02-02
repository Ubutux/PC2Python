"""
Problema 1:

Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""

inicio = 1500
fin = 2700

# Recorremos el rango
for numero in range(inicio, fin + 1):
    # Comprobamos si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # Imprimimos el número
        print(numero)


"""
Problema 1:
Escriba un programa en Python para construir el siguiente patrón.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

h = 5
for i in range(h):
    print("*" * (i + 1))

for i in range(h - 1, 0, -1):
    print("*" * i )

"""
Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
......
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
"""

numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta.upper() == "NO":
        break
    else:
        print("Respuesta inválida. Por favor, responda SI o NO.")

numeros_pares = sum(1 for num in numeros if num % 2 == 0)
numeros_impares = len(numeros) - numeros_pares

print("Números ingresados:", numeros)
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)

"""
problema4

Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad.
"""

# Función para ingresar las calificaciones de un alumno
def ingresar_calificaciones():
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación: "))
    nota2 = float(input("Ingrese la segunda calificación: "))
    nota3 = float(input("Ingrese la tercera calificación: "))
    return {"Alumno": nombre, "Notas": [nota1, nota2, nota3]}

# Función para mostrar el listado completo de alumnos
def mostrar_listado(alumnos):
    print("Listado de alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Inicializar la lista de alumnos
alumnos = []

# Solicitar la cantidad de alumnos a ingresar
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Ingresar los datos de cada alumno
for _ in range(cantidad_alumnos):
    alumno = ingresar_calificaciones()
    alumnos.append(alumno)

# Mostrar el listado completo de alumnos
mostrar_listado(alumnos)

"""
Problema 5

Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count.
"""

def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad

numero_ingresado = int(input("Ingrese el número: "))
digito = int(input("Ingrese el digito: "))
cantidad = contar_digitos(numero_ingresado, digito)
print(f"Cantidad de veces {digito} en el número {numero_ingresado}: {cantidad}")

"""
Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""

n = 50
a = 0
b = 1
print(a)
print(b)
for i in range(0, n-2):
    aux = a + b  
    print(aux)
    a = b
    b = aux
"""
Problema 7:
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.
"""
n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")

"""
Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
"""

n = int(input('ingrese el factorial a calcular: '))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print (fact)

"""
Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
-
-
Input: Twitter
Output: Twttr
Input: What's your name? Output: Wht's yr nm?
"""
def omitir_vocales(cadena):
    vocales = "AEIOUaeiou"
    resultado = ""
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    return resultado

texto = input("Ingrese una cadena de texto: ")
print("Texto sin vocales:", omitir_vocales(texto))

"""
En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
"""

def convertir_fecha(fecha):
    # Definir los nombres de los meses
    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    # Dividir la fecha en partes
    partes = fecha.split()
    # Verificar el formato de entrada y extraer el día, mes y año
    if len(partes) == 3:  
        mes = partes[0]
        dia = partes[1][:-1]  
        año = partes[2]
    else:  # Formato: 9/8/1636
        dia, mes, año = fecha.split("/")
        mes = meses[int(mes) - 1]  
    
    # Formatear la fecha en AAAA-MM-DD
    if len(dia) == 1:
        dia = f"0{dia}"
    if len(mes) == 1:
        mes = f"0{mes}"
    fecha_formateada = f"{año}-{mes}-{dia}"
    
    return fecha_formateada

# Solicitar al usuario ingresar una fecha
fecha_ingresada = input("Ingrese una fecha (en el formato 'mes/día/año' o 'Mes día, año'): ")

# Convertir la fecha ingresada al formato AAAA-MM-DD
fecha_convertida = convertir_fecha(fecha_ingresada)

# Imprimir la fecha convertida
print("La fecha en formato AAAA-MM-DD es:", fecha_convertida)