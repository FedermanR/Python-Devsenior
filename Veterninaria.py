from abc import ABC, abstractmethod

# --- 1. CLASES DE IDENTIDAD (PERSONA Y ROLES) ---
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"Recepcionista"
        
    def registrar_cliente(self):
        return f"El recepcionista está registrando datos..."

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad 

    def mostrar_rol(self):
        return f"Veterinario: Dr. {self.nombre} (Esp: {self.especialidad})"
        
    def atender_mascota(self):
        return f"Iniciando atención médica con Dr. {self.nombre}..."

class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_rol(self):
        return "Rol: Cliente / Propietario"
        
    def mostrar_perfil(self):
        return f"CLIENTE: {self.nombre} | Doc: {self.documento} | Tel: {self.telefono}"

# --- 2. CLASES SECUNDARIAS (MASCOTA Y TRATAMIENTO) ---
class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias
        
    def mostrar_tratamiento(self):
        return f"- {self.nombre}: ${self.costo} (Duración: {self.duracion_dias} días)"

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.consulta_actual = None

    def mostrar_info(self):
        return f"MASCOTA: {self.nombre} | {self.especie} | {self.edad} años | {self.peso} kg"

# --- 3. CLASE CONSULTA (OBLIGATORIA: COMPOSICIÓN Y ASOCIACIÓN) ---
class Consulta:
    def __init__(self, mascota, veterinario, motivo):
        self.mascota = mascota 
        self.veterinario = veterinario
        self.motivo = motivo
        self.tratamientos = []

    def crear_tratamiento(self, nombre, costo, duracion):
        nuevo_tratamiento = Tratamiento(nombre, costo, duracion)
        self.tratamientos.append(nuevo_tratamiento)

    def calcular_costo_consulta(self):
        return sum(t.costo for t in self.tratamientos)

    def mostrar_resumen(self):
        print("\n" + "-"*35)
        print("      RESUMEN CLÍNICO      ")
        print("-"*35)
        print(f"Paciente : {self.mascota.nombre} ({self.mascota.especie})")
        print(f"Atendió  : Dr. {self.veterinario.nombre} ({self.veterinario.especialidad})")
        print(f"Motivo   : {self.motivo}")
        print("Tratamientos:")
        for t in self.tratamientos:
            print("  " + t.mostrar_tratamiento())
        print("-"*35)

# --- 4. POLIMORFISMO Y FACTURACIÓN ---
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto_cobrar, monto_ingresado):
        pass

    def validar_monto(self, monto_cobrar, monto_ingresado):
        if monto_ingresado == monto_cobrar:
            return True
        else:
            print(f">>> PAGO RECHAZADO. El valor ingresado no es exacto.")
            return False

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto_cobrar, monto_ingresado):
        if self.validar_monto(monto_cobrar, monto_ingresado):
            print(">>> PAGO EXITOSO. Recibo de caja generado (Efectivo).")
            return True
        return False

class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto_cobrar, monto_ingresado):
        if self.validar_monto(monto_cobrar, monto_ingresado):
            print(">>> PAGO EXITOSO. Transacción aprobada (Tarjeta).")
            return True
        return False

class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto_cobrar, monto_ingresado):
        if self.validar_monto(monto_cobrar, monto_ingresado):
            print(">>> PAGO EXITOSO. Comprobante bancario validado (Transferencia).")
            return True
        return False

class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19
        self.total = self.subtotal + self.impuesto

    def pagar(self, metodo_pago, monto_ingresado):
        return metodo_pago.procesar_pago(self.total, monto_ingresado)

# --- 5. BASE DE DATOS TEMPORAL ---
inventario_clientes = []
todas_las_mascotas = []

# --- FUNCIONES DE SEGURIDAD (VALIDACIÓN) ---
def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: Ingrese un valor positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def leer_opcion(mensaje, rango_max):
    while True:
        valor = leer_entero(mensaje)
        if 0 <= valor < rango_max:
            return valor
        print(f"Error: Opción inválida. Ingrese un número entre 0 y {rango_max - 1}.")

# --- 6. SISTEMA INTERACTIVO ---
while True:
    print("\n" + "="*45)
    print("      HOSPITAL VETERINARIO - ACCESO")
    print("="*45)
    print("1. Entrar como RECEPCIONISTA")
    print("2. Entrar como VETERINARIO")
    print("3. PROCESAR PAGO (Facturación)")
    print("4. Salir")
    
    perfil = input("Seleccione su perfil: ")

    if perfil == "1":
        # ROL RECEPCIONISTA
        print("\n--- [MODULO 1] Registro de Propietario ---")
        nom_c = input("Nombre del Cliente: ")
        doc_c = input("Documento: ")
        tel_c = input("Teléfono de contacto: ")
        nuevo_cliente = Cliente(nom_c, doc_c, tel_c)
        
        print("\n--- [MODULO 2] Ingreso de Mascota ---")
        nom_m = input("Nombre del paciente (Mascota): ")
        esp_m = input("Especie: ")
        edad_m = leer_entero("Edad (Años enteros): ")
        peso_m = leer_float("Peso (Kg decimal): ")
        
        nueva_mascota = Mascota(nom_m, esp_m, str(edad_m), str(peso_m))
        
        nuevo_cliente.agregar_mascota(nueva_mascota)
        inventario_clientes.append(nuevo_cliente)
        todas_las_mascotas.append(nueva_mascota)
        print(f"\n¡Éxito! El paciente {nueva_mascota.nombre} fue asignado al propietario {nuevo_cliente.nombre}.")

    elif perfil == "2":
        # ROL VETERINARIO
        if not todas_las_mascotas:
            print("No hay mascotas en la sala de espera.")
            continue
            
        print("\n--- [MODULO VETERINARIA] Identificación ---")
        nom_vet = input("Nombre del Médico Veterinario: ")
        doc_vet = input("Documento / Matrícula: ")
        esp_vet = input("Especialidad médica: ")
        vet_actual = Veterinario(nom_vet, doc_vet, esp_vet)
        
        print(f"\nBienvenido, {vet_actual.mostrar_rol()}")
        print("\nPacientes esperando atención:")
        for i, m in enumerate(todas_las_mascotas):
            dueno = next((c.nombre for c in inventario_clientes if m in c.mascotas), "Desconocido")
            print(f"{i}. {m.mostrar_info()} | Dueño: {dueno}")
        
        idx = leer_opcion("\nSeleccione el número del paciente a atender: ", len(todas_las_mascotas))
        mascota_act = todas_las_mascotas[idx]
        
        # Gestión de la Consulta
        if not mascota_act.consulta_actual:
            motivo = input(f"Motivo de consulta para {mascota_act.nombre}: ")
            mascota_act.consulta_actual = Consulta(mascota_act, vet_actual, motivo)
        else:
            print(f"\nEl paciente ya tiene una historia abierta.")
            mascota_act.consulta_actual.mostrar_resumen()
            op = input("\n¿Desea agregar un nuevo tratamiento a esta consulta? (s/n): ")
            if op.lower() != 's':
                continue

        # Formulario de Tratamiento
        print(f"\n--- Recetando a {mascota_act.nombre} ---")
        t_nom = input("Nombre del procedimiento/medicamento: ")
        t_costo = leer_float("Costo del tratamiento: $")
        t_duracion = leer_entero("Duración estimada (días enteros): ")
        
        mascota_act.consulta_actual.crear_tratamiento(t_nom, t_costo, str(t_duracion))
        print("Tratamiento guardado exitosamente.")

    elif perfil == "3":
        # MÓDULO DE PAGO
        print("\n--- [MODULO DE FACTURACIÓN] ---")
        for i, m in enumerate(todas_las_mascotas):
            medico = m.consulta_actual.veterinario.nombre if m.consulta_actual else "N/A"
            estado = f"Atendido por Dr. {medico}" if m.consulta_actual and m.consulta_actual.tratamientos else "SIN PENDIENTES"
            print(f"{i}. {m.nombre} - {estado}")
        
        if not todas_las_mascotas:
            print("No hay registros en el sistema.")
            continue

        idx = leer_opcion("\nSeleccione paciente para procesar cobro: ", len(todas_las_mascotas))
        m_pago = todas_las_mascotas[idx]
        
        if not m_pago.consulta_actual or not m_pago.consulta_actual.tratamientos:
            print("El paciente no registra deudas en el sistema.")
        else:
            m_pago.consulta_actual.mostrar_resumen()
            
            factura_act = Factura(m_pago.consulta_actual)
            print(f"\nSubtotal Tratamientos : ${factura_act.subtotal:.2f}")
            print(f"Impuestos (19%)       : ${factura_act.impuesto:.2f}")
            print(f"TOTAL EXACTO A PAGAR  : ${factura_act.total:.2f}")
            
            print("\nMétodos de pago:")
            print("1. Efectivo | 2. Tarjeta | 3. Transferencia")
            
            # Validamos que elija una opción válida de pago (1, 2 o 3)
            while True:
                tipo_pago = input("Seleccione: ")
                if tipo_pago in ['1', '2', '3']:
                    break
                print("Opción inválida. Ingrese 1, 2 o 3.")

            monto_cliente = leer_float("Ingrese el monto EXACTO: $")
            
            cajero = None
            if tipo_pago == "1": cajero = PagoEfectivo()
            elif tipo_pago == "2": cajero = PagoTarjeta()
            elif tipo_pago == "3": cajero = PagoTransferencia()

            if factura_act.pagar(cajero, monto_cliente):
                m_pago.consulta_actual = None
                print("--- ALTA MÉDICA GENERADA ---")

    elif perfil == "4":
        print("Cerrando sesión en el sistema...")
        break
    else:
        print("Opción de menú inválida. Por favor, seleccione un número del 1 al 4.")