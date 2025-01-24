import random

def bienvenido(func):
    def wrapper(*args, **kwargs):
        print("\n" + "-" * 32)
        func(*args, **kwargs)
        print("_" * 32 + "\n")
    return wrapper

@bienvenido
def mensaje_de_inicio():
    print("Qué gusto tenerte en este juego interactivo llamado: Adivina la Palabra.🎉\n En esta categoría las palabras por adivinar son referentes a algunas de las provincias de Costa Rica.🌎")
    print("¿Listo para poner a prueba tus conocimientos de Geografía Internacional?\n \t Comencemos...")

def palabra_secreta():
    palabras = ["guanacaste", "puntarenas", "cartago", "heredia", "alajuela", "limon"]
    return random.choice(palabras)

def adivina_la_palabra():
    palabra = palabra_secreta()
    vidas = 6
    letras_correctas = []
    letras_incorrectas = []
    secret = ["_" for _ in palabra]

    mensaje_de_inicio()

    while vidas > 0:
        print("\nPalabra secreta:", " ".join(secret))
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        print(f"Número de vidas sobrantes: {vidas}")
      
        salir = input("\nSi desea abandonar la partida, escriba 'salir'. Sino, presione Enter para continuar la partida: ").lower()
        if salir == "salir":
            print("¡Lo intentó muy bien! ¡Nos vemos pronto!")
            break

        letra = input("Ingrese la letra de su interés: ").lower()

        if not letra or letra.isspace():
            print("La entrada no es válida. Por favor, intente nuevamente (solo cadena de texto, y sin vacíos).")
            continue

        if len(letra) != 1:
            print("Tiene permitido ingresar solo UNA letra, intente de nuevo.")
            continue

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Esa letra ya fue ingresada, intente con una diferente.")
            continue

        if letra in palabra:
            print(f"¡Maravilloso! '{letra}' está en la palabra por adivinar.")
            letras_correctas.append(letra)

            secret = [
                letra if palabra[i] == letra else secret[i]
                for i in range(len(palabra))
            ]
            if "_" not in secret:
                print("\n¡Felicidades, lo hizo increíble! Adivinó la palabra:", palabra)
                break
        else:
            print(f"Lamentablemente '{letra}' no está en la palabra del juego.")
            letras_incorrectas.append(letra)
            vidas -= 1

    if vidas == 0:
        print("\nLo lamento, se agotaron sus oportunidades y se quedó sin vidas. La palabra correcta era:", palabra)

@bienvenido
def jugar_nuevamente():
    while True:
        respuesta = input("¿Desea seguir jugando con una palabra diferente? (s/n): ").lower()
        if respuesta == "s":
            adivina_la_palabra()
        elif respuesta == "n":
            print("Agradecemos por dedicarnos un poco de su tiempo en nuestro juego.")
            break
        else:
            print("Nuevamente, ingrese 's' para sí o 'n' para no y abandonar la partida.")

if __name__ == "__main__":
    adivina_la_palabra()
    jugar_nuevamente()