import secrets   # Para generar contraseñas de forma segura
import string    # Contiene letras, dígitos y símbolos


def generar_contrasena(longitud: int, usar_numeros: bool, usar_mayusculas: bool) -> str:
    """
    Genera una contraseña segura con opciones de números y mayúsculas.
    
    Args:
        longitud (int): longitud de la contraseña.
        usar_numeros (bool): incluir números en la contraseña.
        usar_mayusculas (bool): incluir letras mayúsculas.
    
    Returns:
        str: contraseña generada aleatoriamente.
    """
    # 1. Comenzamos con letras minúsculas
    caracteres = string.ascii_lowercase

    # 2. Añadir mayúsculas si el usuario lo desea
    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    # 3. Añadir números si el usuario lo desea
    if usar_numeros:
        caracteres += string.digits

    # 4. Añadir símbolos especiales siempre
    caracteres += string.punctuation

    # 5. Generar contraseña aleatoria utilizando secrets (más seguro que random)
    return "".join(secrets.choice(caracteres) for _ in range(longitud))


def preguntar_si_no(mensaje: str) -> bool:
    """
    Función que pregunta al usuario una opción Sí/No y valida la respuesta.
    
    Args:
        mensaje (str): texto de la pregunta.
    
    Returns:
        bool: True si la respuesta es 's', False si es 'n'.
    """
    while True:  # Repetir hasta que el usuario ingrese una respuesta válida
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta == "s":  # Sí
            return True
        elif respuesta == "n":  # No
            return False
        else:
            print("❌ Respuesta inválida. Debes escribir 's' para Sí o 'n' para No.")


def pedir_longitud(minimo: int = 8, maximo: int = 32) -> int:
    """
    Pide al usuario la longitud de la contraseña y valida que esté dentro del rango permitido.
    
    Args:
        minimo (int): longitud mínima permitida.
        maximo (int): longitud máxima permitida.
    
    Returns:
        int: longitud válida ingresada por el usuario.
    """
    while True:
        valor = input(f"👉 Ingresa la longitud de la contraseña ({minimo}-{maximo}): ").strip()
        if not valor.isdigit():  # Verificar que sea un número
            print("❌ Debes ingresar un número válido.")
            continue
        longitud = int(valor)
        if longitud < minimo or longitud > maximo:  # Validar rango
            print(f"❌ La longitud debe estar entre {minimo} y {maximo}.")
            continue
        return longitud


def main():
    print("🔐 Generador de Contraseñas Seguras")

    # 1. Pedir longitud de la contraseña dentro del rango
    longitud = pedir_longitud()

    # 2. Preguntar si se incluyen números
    usar_numeros = preguntar_si_no("¿Quieres incluir números?")

    # 3. Preguntar si se incluyen letras mayúsculas
    usar_mayusculas = preguntar_si_no("¿Quieres incluir letras mayúsculas?")

    # 4. Generar la contraseña con las opciones seleccionadas
    contrasena = generar_contrasena(longitud, usar_numeros, usar_mayusculas)

    # 5. Mostrar la contraseña generada
    print(f"\n✅ Tu contraseña es: {contrasena}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()


