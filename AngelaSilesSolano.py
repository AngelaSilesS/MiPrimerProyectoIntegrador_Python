
import random      # Se importa la herramienta random para que nos genere las palabras secretas de manera aleatoria.

def bienvenido(func):    # Se define un decorador llamado 'bienvenido'.
    def wrapper(*args, **kwargs):  # Se define una funcion llamada 'wrapper' que nos envuelve a la función original.
        print("\n" + "-" * 50)    # Por elección propia; Imprime una linea divisoria a modo de diseño.
        func(*args, **kwargs)     # Llamamos a la función original que pasa como argumento al decorador. 
        print("_" * 50 + "\n")    # Por elección propia; Imprime una linea divisoria a modo de diseño. x2
    return wrapper              # Returnamos a la función decorada 'wrapper'.

@bienvenido               # Hacemos un llamado a nuestro decorador 'bienvenido.'
def mensaje_de_inicio():     # Creamos una función que está decorada con 'bienvenido', y en ella se define el mensaje que deseamos mostrarle al usuario al inicio del juego.
    print("Qué gusto tenerte en este juego interactivo llamado: Adivina la Palabra.🎉\nEn esta categoría, las palabras por adivinar están relacionadas a algunas de las provincias de Costa Rica.🌎")
    print("¿Listo para poner a prueba tus conocimientos de Geografía Internacional?\n \t Comencemos...")

def palabra_secreta():   # Función que va a contener nuestras palabras por adivinar.
    palabras = ["guanacaste", "puntarenas", "cartago", "heredia", "alajuela", "limon"] # Lista que contiene nuestras palabras secretas, en este caso son 7.
    return random.choice(palabras)    # Se returna de manera aleatoria una de las 7 palabras definidas anteriormente.
# El random.choice nos extrae un elemento aleatorio directamente de la secuencia de palabras en la lista.

def adivina_la_palabra():  # Función que será una de las principales del juego.
    palabra = palabra_secreta()  # Contiene una de las palabras por adivinar.
    vidas = 6                    # Se define el número límite inicial de vidas / intentos del usuario.
    letras_correctas = []        # Lista donde estarán almacenadas las letras que se adivinen correctamente.
    letras_incorrectas = []      # Lista donde estarán almacenadas las letras que se adivinen incorrectamente.
    secret = ["_" for _ in palabra]  # Representa cada letra de la palabra secreta mediante un guión bajo.

    mensaje_de_inicio()     # Llama a la función decorada que contiene nuestro mensaje inicial para el usuario.

    while vidas > 0:        # Se inicia el bucle principal de nuestro juego.
        print("\nPalabra secreta:", " ".join(secret))     # Nos va mostrando en la terminal cada actualización de nuestra palabra secreta, representada por guión, o la letra adivinada.
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}") # Se muestra en la terminal las letras que hemos ingresado y que no son correctas.
        print(f"Número de vidas sobrantes: {vidas}")                 # Le informa al usuario cuantas vidas / intentos le quedan.
      
        letra = input("Ingrese la letra de su interés: ").strip().lower()  # Le indica al usuario que debe ingresar la letra que desee; Nos devuelve la letra sin espacios, y las letras en minúscula.
        if not letra.isalpha():         # Verifica que el usuario ingrese solo letras, prohibiendo los números o caracteres especiales.
           print("\nLa entrada no es válida. Por favor, intente nuevamente (solo letras y sin vacíos).")  # Y muestra este mensaje.
           continue  # La iteración actual se interrumpe, y pasa a la iteración superior solicitando la letra nuevamente. 
                
        if len(letra) != 1:            # Verifica que se ingrese solo una letra.
            print("Tiene permitido ingresar solo UNA letra, intente de nuevo.") # Y muestra este mensaje.
            continue         # La iteración actual se interrumpe, y pasa a la iteración superior solicitando la letra nuevamente.

        if letra in letras_correctas or letra in letras_incorrectas: # Verifica si la letra ingresada está en la lista de letras correctas/incorrectas, así se evita la repetición de letra.
            print("Esa letra ya fue ingresada, intente con una diferente.") # Y muestra este mensaje.
            continue         # La iteración actual se interrumpe, y pasa a la iteración superior solicitando la letra nuevamente.

        if letra in palabra:    # Verifica si la letra ingresada está en la palabra por adivinar.
            print(f"¡Maravilloso! '{letra}' está en la palabra por adivinar.")   # Imprime este mensaje de felicitación.
            letras_correctas.append(letra)    # Con este código agregamos la letra a la lista de letras correctas.

            secret = [                                  # Es una comprensión de listas, que nos ayuda a actualizar la lista de palabras secreta representada por guiones bajos.
                letra if palabra[i] == letra else secret[i]   # A medida que el jugador adivina correctamente, los guiones bajos correspondientes se reemplazan con las letras correctas.
                for i in range(len(palabra))
            ]
            if "_" not in secret:         # Verifica si el usuario logró completar la palabra secreta.
                print("\n¡Felicidades, lo hizo increíble! Adivinó la palabra:", palabra) # Imprime este mensaje de felicitación.
                break                 # Y cierra el bucle si se cumple la condición anterior.
        else:                        # De lo contrario...
            print(f"Lamentablemente '{letra}' no está en la palabra del juego.") # Imprime este mensaje.
            letras_incorrectas.append(letra)               # Agrega la letra a la lista de letras incorrectas. 
            vidas -= 1            # Y se resta una vida / intento.

    if vidas == 0:                  # Si el número de vidas llega al número 0...
        print("\nLo lamento, se agotaron sus oportunidades y se quedó sin vidas. La palabra correcta era:", palabra) # Imprime este mensaje.

@bienvenido           # Hacemos otro llamado a nuestro decorador 'bienvenido.'
def jugar_nuevamente():       # Con esta función le damos la oportunidad al usuario de....
    while True:               #Iniciar un nuevo ciclo de intento.
        respuesta = input("¿Desea seguir jugando con una palabra diferente? (s/n): ").lower()  #Solicitamos al usuario una respuesta a este mensaje...
        if respuesta == "s":         # Si la respuesta es 's'...
            adivina_la_palabra()     # Volvemos al ciclo del juego, e iniciamos con una palabra distinta a la anterior.
        elif respuesta == "n":       # Si la respuesta es 'n'...
            print("Agradecemos por dedicarnos un poco de su tiempo en nuestro juego.") #Imprime este mensaje al usuario.
            break          # Y el ciclo se rompe.
        else:             # Si el usuario ingresa algo distinto a 's / n'...
            print("Nuevamente, ingrese 's' para sí o 'n' para no y abandonar la partida.")  #Imprime este mensaje al usuario.

@bienvenido         # Hacemos nuevamente el llamado a nuestro decorador 'bienvenido.'
def active_game ():      # Creamos una función que contenga...
    adivina_la_palabra()   # El ciclo principal de nuestro juego.
    jugar_nuevamente()     # Y el llamado a la oportunidad al usuario de elegir si desea jugar otra vez o no.

active_game ()    # Llamamos a nuestra función principal, que nos estará imprimiendo todo el código anterior.