from datetime import datetime

ARCHIVO = "usuarios.txt"

def obtener_lineas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []

def guardar_lineas(lineas):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

def es_nombre_valido(nombre):
    if nombre == "":
        return False
    for caracter in nombre.replace(" ", ""):
        if not caracter.isalpha():
            return False
    return True

def usuario_existe(nombre_buscar):
    lineas = obtener_lineas()
    for linea in lineas:
        datos = linea.strip().split(",")
        if datos and datos[0].lower() == nombre_buscar.lower():
            return True
    return False

def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario:").strip()

        if not es_nombre_valido(nombre):
            print("Nombre invalido. Solo se permiten letras sin caracteres especiales.")
            return

        if usuario_existe(nombre):
            print("El usuario ya existe. No se permiten duplicados.")
            return

        edad_str = input("Ingrese la edad del usuario:")
        if not edad_str.isdigit():
            print("La edad debe ser un valor numerico positivo.")
            return
            
        edad = int(edad_str)
        if edad < 1 or edad > 120:
            print("La edad debe estar en el rango de 1 a 120 anos.")
            return

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha}\n")
        print("Usuario registrado exitosamente.")

    except PermissionError:
        print("No se tienen permisos para escribir en el archivo.")
    except Exception as error:
        print(f"Ocurrio un error inesperado: {error}")

def mostrar_usuarios():
    lineas = obtener_lineas()
    if not lineas:
        print("No hay usuarios registrados.")
        return

    print("\nUsuarios registrados:")
    suma_edades = 0
    
    for i, linea in enumerate(lineas, 1):
        datos = linea.strip().split(",")
        nombre = datos[0]
        edad = int(datos[1])
        suma_edades += edad
        
        if len(datos) > 2:
            fecha = datos[2]
        else:
            fecha = "Sin fecha"
            
        print(f"[{i}] Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")

    total_usuarios = len(lineas)
    promedio_edad = suma_edades / total_usuarios
    
    print("\nEstadisticas:")
    print(f"Total de usuarios registrados: {total_usuarios}")
    print(f"Edad promedio: {promedio_edad:.2f} anos")

def buscar_usuario():
    try:
        busqueda = input("Ingrese el nombre a buscar:").strip().lower()
        encontrado = False
        lineas = obtener_lineas()

        for i, linea in enumerate(lineas, 1):
            datos = linea.strip().split(",")
            nombre = datos[0]
            if busqueda in nombre.lower():
                edad = datos[1]
                if len(datos) > 2:
                    fecha = datos[2]
                else:
                    fecha = "Sin fecha"
                print(f"[{i}] Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")
                encontrado = True

        if not encontrado:
            print("Usuario no encontrado.")

    except Exception as error:
        print(f"Ocurrio un error inesperado: {error}")

def modificar_usuario():
    mostrar_usuarios()
    lineas = obtener_lineas()
    if not lineas:
        return
    
    try:
        indice = int(input("\nIngrese el numero del usuario a modificar: ")) - 1
        if indice < 0 or indice >= len(lineas):
            print("Numero de usuario no valido.")
            return
        
        datos = lineas[indice].strip().split(",")
        nombre_actual = datos[0]
        
        nuevo_nombre = input(f"Ingrese el nuevo nombre ({nombre_actual}):").strip()
        if nuevo_nombre == "":
            nuevo_nombre = nombre_actual
        elif not es_nombre_valido(nuevo_nombre):
            print("Nombre invalido.")
            return
        elif nuevo_nombre.lower() != nombre_actual.lower() and usuario_existe(nuevo_nombre):
            print("El nombre ya existe. No se permiten duplicados.")
            return

        nueva_edad_str = input(f"Ingrese la nueva edad ({datos[1]}):").strip()
        if nueva_edad_str == "":
            nueva_edad = int(datos[1])
        elif not nueva_edad_str.isdigit():
            print("La edad debe ser un valor numerico.")
            return
        else:
            nueva_edad = int(nueva_edad_str)
            if nueva_edad < 1 or nueva_edad > 120:
                print("La edad debe estar entre 1 y 120.")
                return
        
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lineas[indice] = f"{nuevo_nombre},{nueva_edad},{fecha}\n"
        guardar_lineas(lineas)
        print("Usuario modificado exitosamente.")
        
    except ValueError:
        print("Entrada invalida. Debe ingresar valores numericos.")
    except Exception as error:
        print(f"Ocurrio un error inesperado: {error}")

def eliminar_usuario():
    try:
        nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ").strip().lower()
        lineas = obtener_lineas()
        
        if not lineas:
            print("No hay usuarios para eliminar.")
            return
            
        nuevas_lineas = []
        eliminado = False
        
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0].lower() == nombre_eliminar:
                eliminado = True
            else:
                nuevas_lineas.append(linea)
                
        if eliminado:
            guardar_lineas(nuevas_lineas)
            print("Usuario eliminado exitosamente. La lista se ha reordenado.")
        else:
            print("No se encontro un usuario con ese nombre.")
            
    except Exception as error:
        print(f"Ocurrio un error inesperado: {error}")

def ordenar_usuarios():
    lineas = obtener_lineas()
    if not lineas:
        print("No hay usuarios para ordenar.")
        return

    print("\nCriterios de ordenamiento:")
    print("1. Ordenar por nombre")
    print("2. Ordenar por edad")
    opcion = input("Seleccione una opcion: ").strip()

    try:
        if opcion == "1":
            lineas.sort(key=lambda x: x.split(",")[0].lower())
            print("Usuarios ordenados por nombre alfabeticamente.")
        elif opcion == "2":
            lineas.sort(key=lambda x: int(x.split(",")[1]))
            print("Usuarios ordenados por edad de menor a mayor.")
        else:
            print("Opcion no valida.")
            return

        guardar_lineas(lineas)
    except Exception as error:
        print(f"Ocurrio un error al intentar ordenar: {error}")

def validar_linea(linea):
    linea = linea.strip()
    if not linea:
        return False, "Linea vacia"

    datos = linea.split(",")
    if len(datos) < 2:
        return False, "Faltan datos"

    nombre = datos[0].strip()
    edad_str = datos[1].strip()

    if not es_nombre_valido(nombre):
        return False, "El nombre contiene numeros, caracteres especiales o esta vacio"
    
    if not edad_str.isdigit():
        return False, "La edad no es numerica o es negativa"
    
    edad = int(edad_str)
    if edad < 1 or edad > 120:
        return False, "La edad no esta en el rango de 1 a 120"

    return True, "Correcto"

def validar_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo a validar:")
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            hay_errores = False
            for i, linea in enumerate(archivo, 1):
                es_valida, mensaje = validar_linea(linea)
                if not es_valida:
                    print(f"Error en linea {i}: {mensaje} -> {linea.strip()}")
                    hay_errores = True
            
            if not hay_errores:
                print("El archivo no tiene errores.")

    except FileNotFoundError:
        print("El archivo indicado no existe.")
    except Exception as error:
        print(f"Ocurrio un error al leer el archivo: {error}")

def crear_archivo_errores():
    archivo_origen = input("Ingrese el nombre del archivo a procesar:")
    archivo_buenos = "registros_buenos.txt"
    archivo_malos = "registros_malos.txt"

    try:
        with open(archivo_origen, "r", encoding="utf-8") as origen, \
             open(archivo_buenos, "w", encoding="utf-8") as buenos, \
             open(archivo_malos, "w", encoding="utf-8") as malos:

            for linea in origen:
                es_valida, _ = validar_linea(linea)
                if es_valida:
                    buenos.write(linea)
                else:
                    malos.write(linea)

        print("Proceso terminado. Se crearon registros_buenos.txt y registros_malos.txt")

    except FileNotFoundError:
        print("El archivo indicado no existe.")
    except Exception as error:
        print(f"Ocurrio un error al procesar el archivo: {error}")

def menu():
    opcion = ""
    while opcion != "9":

        print("\n==== MENU DE USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios y estadisticas")
        print("3. Buscar usuario")
        print("4. Modificar usuario por numero")
        print("5. Eliminar usuario por nombre")
        print("6. Ordenar lista de usuarios")
        print("7. Validar un archivo externo")
        print("8. Crear archivo de buenos y malos")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            modificar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            ordenar_usuarios()
        elif opcion == "7":
            validar_archivo()
        elif opcion == "8":
            crear_archivo_errores()
        elif opcion == "9":
            print("Programa finalizado.")
        else:
            print("Opcion no valida. Intente nuevamente.")

menu()