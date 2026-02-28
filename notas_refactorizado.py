"""
Programa de gestión de notas de alumnos.
Calcula la media de tres notas, determina si está aprobado
y muestra la calificación cualitativa correspondiente.

Autor: Francisco López
Fecha: 26/02/2026
"""

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.

    Returns:
        float: Media de las tres notas.
    """
    return (nota1 + nota2 + nota3) / 3


def esta_aprobado(media):
    """
    Determina si una nota media está aprobada.

    Args:
        media (float): Nota media del alumno.

    Returns:
        bool: True si está aprobado, False si está suspendido.
    """
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def obtener_calificacion(media):
    """
    Devuelve la calificación cualitativa según la nota media.

    Args:
        media (float): Nota media.

    Returns:
        str: Calificación textual.
    """
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_alumno(nombre, nota1, nota2, nota3):
    """
    Muestra por pantalla la información completa de un alumno.

    Args:
        nombre (str): Nombre del alumno.
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    """
    print(f"Alumno: {nombre}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    media = calcular_media(nota1, nota2, nota3)  # Se reutiliza la función extraída
    print(f"Media: {media}")

    print(obtener_calificacion(media))  # Se delega la lógica de clasificación
    print("----------------------")


def main():
    """Función principal que ejecuta el programa."""
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()