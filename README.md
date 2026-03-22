Ejercicio práctico (2 horas)
Sistema de Gestión Básica de Estudiantes
Contexto

Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma simple desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre

Edad

Nota 1

Nota 2

Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre

edad

3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"

"En recuperación"

"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5

Que la edad sea mayor que 0

Si los datos no son válidos, debe pedirlos nuevamente.

Parte final (obligatoria)

Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X