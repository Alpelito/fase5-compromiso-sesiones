# Fase 5 – Evaluación Final POA · Problema 1

**Universidad Nacional Abierta y a Distancia – UNAD**

- **Curso:** Fundamentos de Programación (213022)
- **Grupo:** 213022_993
- **Estudiante:** José Alfonso Peñaranda Lozano

## Descripción del problema

Una matriz almacena datos de sesiones de clientes en una plataforma digital con el formato por fila:

```
[ID del cliente, Duración de la sesión (en segundos), Número de clics]
```

El programa evalúa el **nivel de compromiso** de cada sesión con estas reglas:

| Nivel | Condición |
|-------|-----------|
| **Alto** | Duración > 180 segundos **y** clics > 8 |
| **Bajo** | Duración < 60 segundos **o** clics < 3 |
| **Medio** | Cualquier otro caso |

## Cómo ejecutar

Requiere Python 3.8 o superior.

```bash
python fase5_problema1_compromiso.py
```

Menú del programa:

1. Ver informe de compromiso (ID del cliente y su clasificación, con resumen por nivel)
2. Registrar nueva sesión (valida que el ID no esté vacío ni repetido y que los valores sean enteros ≥ 0)
3. Consultar un cliente por su ID
4. Salir

## Estructuras utilizadas

| Estructura | Dónde se usa |
|------------|--------------|
| Secuenciales | Constantes de umbral, asignaciones, entradas (`input`) y salidas (`print`) |
| De control | `if / elif / else` con `and` / `or` en `clasificar_compromiso()`; menú en `main()` |
| Repetitivas | `for` para recorrer la matriz; `while` para el menú y la validación de datos |
| Arreglos | Matriz (lista de listas) con 8 sesiones iniciales |
| Funciones | `clasificar_compromiso()`, `contar_por_nivel()`, `mostrar_informe()`, `buscar_sesion()`, `registrar_sesion()`, entre otras |

## Ejemplo de salida

```
No.  ID cliente    Duración (s)   Clics   Compromiso
----------------------------------------------------------
1    CLI-001                250      12   Alto
2    CLI-002                 45      10   Bajo
3    CLI-003                120       5   Medio
4    CLI-004                200       2   Bajo
5    CLI-005                181       9   Alto
6    CLI-006                180      15   Medio
7    CLI-007                 60       3   Medio
8    CLI-008                300       8   Medio
----------------------------------------------------------
Total de sesiones evaluadas: 8
  Alto :   2  (25.0 %)
  Medio:   4  (50.0 %)
  Bajo :   2  (25.0 %)
```
