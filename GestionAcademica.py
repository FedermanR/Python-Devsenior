# ==========================================
# SISTEMA DE GESTIÓN ACADÉMICA - UNIVERSIDAD
# Enfoque: Ingeniería de Sistemas
# ==========================================

# --- FUNCIONES OBLIGATORIAS ---

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"

def registrar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante: ")
    
    # Validar edad
    while True:
        edad = int(input("Ingrese la edad: "))
        if edad > 0: break
        print("Error: La edad debe ser mayor a 0.")
    
    # Validar 3 notas
    notas = []
    for i in range(1, 4):
        while True:
            n = float(input(f"Ingrese nota {i} (0-5): "))
            if 0 <= n <= 5:
                notas.append(n)
                break
            print("Error: La nota debe estar entre 0 y 5.")
            
    return nombre, notas

# --- LÓGICA PRINCIPAL (Bucle de control) ---

total_estudiantes = 0
suma_promedios = 0

while True:
    print("\n===== SISTEMA DE ESTUDIANTES =====")
    print("1. Registrar estudiante")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # Ejecutar registro y cálculos
        nombre, mis_notas = registrar_estudiante()
        promedio = calcular_promedio(mis_notas[0], mis_notas[1], mis_notas[2])
        estado = evaluar_estado(promedio)
        
        # Acumular datos para el resumen
        total_estudiantes += 1
        suma_promedios += promedio
        
        # Mostrar resultado individual
        print(f"Promedio del estudiante: {promedio:.2f}")
        print(f"Estado académico: {estado}")
        
    elif opcion == "2":
        # Mostrar resumen final antes de salir
        if total_estudiantes > 0:
            promedio_grupal = suma_promedios / total_estudiantes
            print("\n--- RESUMEN FINAL ---")
            print(f"Total de estudiantes registrados: {total_estudiantes}")
            print(f"Promedio general del grupo: {promedio_grupal:.2f}")
        else:
            print("\nNo se registraron estudiantes.")
        break
    else:
        print("Opción no válida.")