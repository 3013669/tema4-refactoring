def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def esta_aprobado(media):
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def obtener_calificacion(media):
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_alumno(nombre, nota1, nota2, nota3):
    print(f"Alumno: {nombre}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    media = calcular_media(nota1, nota2, nota3)  # Se reutiliza la función extraída
    print(f"Media: {media}")

    print(obtener_calificacion(media))  # Se delega la lógica de clasificación
    print("----------------------")


def main():
    mostrar_alumno("Ana García", 8, 7, 9)
    mostrar_alumno("Luis Pérez", 4, 5, 3)
    mostrar_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()