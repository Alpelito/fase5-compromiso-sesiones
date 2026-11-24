# -*- coding: utf-8 -*-
"""
Universidad Nacional Abierta y a Distancia - UNAD
Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI
Curso: Fundamentos de Programación (213022) - Grupo 213022_993
Fase 5 - Evaluación Final POA - Problema 1
Estudiante: José Alfonso Peñaranda Lozano

Descripción:
    Herramienta que evalúa el nivel de compromiso de las sesiones de
    clientes en una plataforma digital. Los datos se guardan en una
    matriz (lista de listas) con el siguiente formato por fila:

        [ID del cliente, Duración de la sesión (en segundos), Número de clics]

    Reglas de negocio:
        - "Alto"  : duración > 180 segundos  y  clics > 8
        - "Bajo"  : duración < 60 segundos   o  clics < 3
        - "Medio" : en cualquier otro caso

Estructuras utilizadas:
    - Secuenciales : constantes, asignaciones, entradas y salidas.
    - De control   : if / elif / else con operadores lógicos and / or.
    - Repetitivas  : for (recorrido de la matriz) y while (menú y validaciones).
    - Funciones    : cada tarea del programa está en una función con parámetros
                     y valor de retorno.
"""

# ---------------------------------------------------------------------------
# CONSTANTES: umbrales de la lógica de negocio
# ---------------------------------------------------------------------------
DURACION_ALTA = 180   # segundos: la duración debe ser MAYOR para "Alto"
CLICS_ALTOS = 8       # clics: deben ser MAYORES para "Alto"
DURACION_BAJA = 60    # segundos: una duración MENOR clasifica como "Bajo"
CLICS_BAJOS = 3       # clics: una cantidad MENOR clasifica como "Bajo"

# Posición de cada dato dentro de una fila de la matriz
COL_ID = 0
COL_DURACION = 1
COL_CLICS = 2


# ---------------------------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------------------------
def crear_matriz_inicial():
    """Crea y retorna la matriz con los datos iniciales (8 sesiones)."""
    sesiones = [
        ["CLI-001", 250, 12],   # Alto: cumple las dos condiciones
        ["CLI-002", 45, 10],    # Bajo: duración menor a 60 s
        ["CLI-003", 120, 5],    # Medio: no es Alto ni Bajo
        ["CLI-004", 200, 2],    # Bajo: menos de 3 clics
        ["CLI-005", 181, 9],    # Alto: justo por encima de ambos umbrales
        ["CLI-006", 180, 15],   # Medio: 180 s no es mayor que 180
        ["CLI-007", 60, 3],     # Medio: 60 s y 3 clics no son menores
        ["CLI-008", 300, 8],    # Medio: 8 clics no es mayor que 8
    ]
    return sesiones


def clasificar_compromiso(duracion, clics):
    """Retorna "Alto", "Medio" o "Bajo" según la duración y los clics."""
    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        nivel = "Alto"
    elif duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        nivel = "Bajo"
    else:
        nivel = "Medio"
    return nivel


def contar_por_nivel(matriz):
    """Recorre la matriz y retorna cuántas sesiones hay de cada nivel."""
    altos = 0
    medios = 0
    bajos = 0
    for fila in matriz:
        nivel = clasificar_compromiso(fila[COL_DURACION], fila[COL_CLICS])
        if nivel == "Alto":
            altos += 1
        elif nivel == "Medio":
            medios += 1
        else:
            bajos += 1
    return altos, medios, bajos


def calcular_porcentaje(cantidad, total):
    """Retorna el porcentaje que representa cantidad sobre total."""
    if total == 0:
        return 0.0
    return cantidad * 100 / total


def mostrar_informe(matriz):
    """Muestra el informe con el ID de cada cliente y su clasificación."""
    print()
    print("=" * 58)
    print("     INFORME DE NIVEL DE COMPROMISO POR SESIÓN")
    print("=" * 58)
    print(f"{'No.':<5}{'ID cliente':<12}{'Duración (s)':>14}{'Clics':>8}   {'Compromiso':<10}")
    print("-" * 58)

    numero = 1
    for fila in matriz:
        nivel = clasificar_compromiso(fila[COL_DURACION], fila[COL_CLICS])
        print(f"{numero:<5}{fila[COL_ID]:<12}{fila[COL_DURACION]:>14}"
              f"{fila[COL_CLICS]:>8}   {nivel:<10}")
        numero += 1

    total = len(matriz)
    altos, medios, bajos = contar_por_nivel(matriz)
    print("-" * 58)
    print(f"Total de sesiones evaluadas: {total}")
    print(f"  Alto : {altos:>3}  ({calcular_porcentaje(altos, total):.1f} %)")
    print(f"  Medio: {medios:>3}  ({calcular_porcentaje(medios, total):.1f} %)")
    print(f"  Bajo : {bajos:>3}  ({calcular_porcentaje(bajos, total):.1f} %)")
    print("=" * 58)


def buscar_sesion(matriz, id_cliente):
    """Retorna la posición de la sesión con ese ID, o -1 si no existe."""
    for posicion in range(len(matriz)):
        if matriz[posicion][COL_ID] == id_cliente:
            return posicion
    return -1


def leer_entero_no_negativo(mensaje):
    """Pide un número entero >= 0 y repite la pregunta hasta que sea válido."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdecimal():        # solo acepta dígitos (entero sin signo)
            return int(dato)
        print("   Valor no válido. Ingrese un número entero igual o mayor a 0.")


def leer_id_nuevo(matriz):
    """Pide un ID que no esté vacío ni repetido en la matriz."""
    id_cliente = input("ID del cliente (ej. CLI-009): ").strip().upper()
    while id_cliente == "" or buscar_sesion(matriz, id_cliente) != -1:
        if id_cliente == "":
            print("   El ID no puede estar vacío.")
        else:
            print(f"   El ID {id_cliente} ya existe. Ingrese uno diferente.")
        id_cliente = input("ID del cliente (ej. CLI-009): ").strip().upper()
    return id_cliente


def registrar_sesion(matriz):
    """Agrega una nueva sesión (fila) a la matriz y muestra su clasificación."""
    print("\n--- Registrar nueva sesión ---")
    id_cliente = leer_id_nuevo(matriz)
    duracion = leer_entero_no_negativo("Duración de la sesión (segundos): ")
    clics = leer_entero_no_negativo("Número de clics: ")

    matriz.append([id_cliente, duracion, clics])
    nivel = clasificar_compromiso(duracion, clics)
    print(f"Sesión registrada. {id_cliente} -> compromiso {nivel}.")


def consultar_cliente(matriz):
    """Busca un cliente por su ID y muestra los datos de su sesión."""
    print("\n--- Consultar cliente ---")
    id_cliente = input("ID del cliente a consultar: ").strip().upper()
    posicion = buscar_sesion(matriz, id_cliente)
    if posicion == -1:
        print(f"No existe una sesión con el ID {id_cliente}.")
    else:
        fila = matriz[posicion]
        nivel = clasificar_compromiso(fila[COL_DURACION], fila[COL_CLICS])
        print(f"ID: {fila[COL_ID]} | Duración: {fila[COL_DURACION]} s | "
              f"Clics: {fila[COL_CLICS]} | Compromiso: {nivel}")


def mostrar_menu():
    """Muestra las opciones del programa."""
    print("\n========== EVALUACIÓN DE COMPROMISO DE SESIONES ==========")
    print("1. Ver informe de compromiso")
    print("2. Registrar nueva sesión")
    print("3. Consultar un cliente")
    print("4. Salir")


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    sesiones = crear_matriz_inicial()
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            mostrar_informe(sesiones)
        elif opcion == "2":
            registrar_sesion(sesiones)
        elif opcion == "3":
            consultar_cliente(sesiones)
        elif opcion == "4":
            print("Programa finalizado. ¡Hasta pronto!")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
