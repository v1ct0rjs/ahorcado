from os import system  # Importa la función system del módulo os
from random import choice  # Importa la función choice del módulo random
from modulos import ahorcado, horca, colorear  # Importa las funciones de los módulos ahorcado, horca y colorear
import time

INTENTOS = 11  # Número de intentos para adivinar la palabra


def generar_palabra(dificultad: int) -> str | None:
    """Genera una palabra aleatoria de un archivo de texto con la dificultad seleccionada
    Args:
        dificultad (int): Nivel de dificultad de la palabra a adivinar
        Returns:    Palabra a adivinar"""

    try:  # Manejo de excepciones
        with open('palabras.txt', mode='r') as file:  # Abre el archivo palabras.txt en modo lectura
            lista_palabras = file.readlines()  # Lee todas las líneas del archivo y las guarda en una lista
            while True:  # Bucle infinito
                palabra = choice(lista_palabras)  # Elige una palabra aleatoria de la lista
                palabra = palabra.strip().replace(' ',
                                                  '').lower()  # Elimina los espacios en blanco y convierte la palabra a minúsculas
                if len(palabra) == dificultad:  # Si la longitud de la palabra es igual a la dificultad seleccionada
                    return palabra  # Devuelve la palabra
    except FileNotFoundError as e:  # Si el archivo no se encuentra, muestra un mensaje de error
        print(f'Error: {e}')  # Muestra el mensaje de error
        return None  # Devuelve None si no se ha podido leer el archivo


def comprobar_entrada(nueva_letra: str, letras_introducidas: list) -> bool:
    """Comprueba si la letra introducida ya ha sido introducida anteriormente
        Args:
        nueva_letra (str): Letra introducida por el usuario
        letras_introducidas (list): Lista de letras introducidas
        Returns: True si la letra ya ha sido introducida, False si no lo ha sido"""

    if nueva_letra in letras_introducidas:  # Si la letra ya ha sido introducida, devuelve True
        return True
    else:
        return False


def get_nueva_letra(letras_introducidas: list) -> str:
    """Obtiene una nueva letra introducida por el usuario
    Args:
        letras_introducidas (list): Lista de letras introducidas
        Returns: Letra introducida por el usuario
        Solo se aceptan letras minúsculas del alfabeto español, sin tildes, diéresis o caracteres especiales"""

    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']  # Lista de caracteres válidos
    while True:  # Bucle infinito
        try:
            letra = input('Introduce una letra >>> ')  # Pide al usuario que introduzca una letra
            letra = letra.lower()  # Convierte la letra a minúsculas
            if letra not in caracteres:  # Si la letra no está en la lista de caracteres válidos
                print('Error: Caracter no válido')  # Muestra un mensaje de error
            else:
                comprobar = comprobar_entrada(letra,
                                              letras_introducidas)  # Comprueba si la letra ya ha sido introducida
                if not comprobar:  # Si la letra no ha sido introducida
                    letras_introducidas.append(letra)  # Añade la letra a la lista de letras introducidas
                    return letra  # Devuelve la letra
        except TypeError as e:  # Manejo de excepciones
            print(f'Error: {e}')
        except ValueError as e:
            print(f'Error: {e}')


def construir_palabra_adivinada(palabra_objetivo: str, letras_introducidas: list) -> str:
    """Construye la palabra a adivinar con las letras introducidas por el usuario
    Args:
        palabra_objetivo (str): Palabra a adivinar
        letras_introducidas (list): Lista de letras introducidas
        Returns: Palabra a adivinar con las letras introducidas por el usuario
        Las letras no introducidas se muestran como guiones bajos"""

    palabra_adivinada = ''  # Inicializa la palabra a adivinar
    introducidas = ''  # Inicializa la lista de letras introducidas
    for letra in palabra_objetivo:  # Bucle para cada letra de la palabra a adivinar
        if letra in letras_introducidas:  # Si la letra está en la lista de letras introducidas
            palabra_adivinada += letra + ' '  # Añade la letra a la palabra a adivinar
        else:
            palabra_adivinada += '_ '  # Añade un guión bajo a la palabra a adivinar

    for i in letras_introducidas:  # Bucle para cada letra introducida
        introducidas += i + ' '  # Añade la letra a la lista de letras introducidas

    colorear.printcolor('amarillo', f'Tu palabra es: {palabra_adivinada}', 'negrita')  # Muestra la palabra a adivinar
    colorear.printcolor('verde', 'Listado de letras introducidas: ',
                        'negrita')  # Muestra el listado de letras introducidas
    colorear.printcolor('rojo', f'>>> {introducidas}', 'negrita')  # Muestra la lista de letras introducidas

    return palabra_adivinada  # Devuelve la palabra a adivinar


def game_over(num_fallos: int, palabra_objetivo: str, letras_introducidas: list) -> bool:
    """Comprueba si el juego ha terminado
    Args:
        num_fallos (int): Número de fallos
        palabra_objetivo (str): Palabra a adivinar
        letras_introducidas (list): Lista de letras introducidas
        Returns: True si el juego ha terminado, False si no ha terminado"""

    if num_fallos >= INTENTOS:  # Si el número de fallos es mayor o igual al número de intentos
        return True  # Devuelve True

    for letra in palabra_objetivo:  # Bucle para cada letra de la palabra a adivinar
        if letra not in letras_introducidas:  # Si la letra no está en la lista de letras introducidas
            return False

    return True  # Devuelve True si el juego ha terminado


def licencia() -> None:
    """Muestra la licencia de uso del programa"""
    try:
        with open('lgpl-3.0.txt', mode='r') as file:  # Abre el archivo lgpl-3.0.txt en modo lectura
            colorear.printcolor('verde', file.read(), 'negrita')  # Muestra el contenido del archivo
    except FileNotFoundError as e:  # Si el archivo no se encuentra, muestra un mensaje de error
        print(f'Error: {e}')


def menu() -> int:
    """Muestra el menú de inicio del juego y permite seleccionar el nivel de dificultad
    Returns: Nivel de dificultad seleccionado"""

    while True:
        colorear.printcolor('cyan', """
                *************************************************
                *                                               *
                *                A H O R C A D O                *
                *                                               *
                *          Victor Manuel Jiménez Sánchez        *
                *         Curso de especialización Python       *
                *             IES. Suarez de Figueroa           *
                *                                               *
                *************************************************
                """, 'negrita', )

        colorear.printcolor('amarillo', """Selecciona el nivel de dificultad:
            
                1: Fácil
                2: Intermedio
                3: Difícil
                4: Experto
                5: Licencia
                0: Salir
                """, 'negrita')

        try:
            opcion = int(input('Introduce el número de la opción >>> '))  # Pide al usuario que introduzca un número
            if opcion in range(0, 6):  # Si el número está en el rango de 0 a 5
                match opcion:  # Comprueba el valor de la variable opcion
                    case 1:
                        return 4
                    case 2:
                        return 5
                    case 3:
                        return 6
                    case 4:
                        return 7
                    case 5:
                        system('clear')
                        licencia()
                        input()
                        system('clear')
                    case 0:
                        return 0
            else:
                print('Error: el valor introducido no es una opción válida')  # Muestra un mensaje de error
        except ValueError:  # Manejo de excepciones
            print('Error: el valor introducido no es un número entero')


def mostrar_tiempo(tiempo):
    """Muestra el tiempo transcurrido desde el inicio del juego
    Args:
        tiempo: Tiempo de inicio del juego"""
    minutos, segundos = divmod(round(time.time() - tiempo), 60) # Calcula los minutos y segundos transcurridos
    colorear.printcolor('magenta',f'{time.strftime("%H:%M:%S", time.gmtime())}    {minutos:02d}:{segundos:02d} Tiempo Transcurrido','parpadeo', 'negrita') # Muestra el tiempo transcurrido


def main():
    while True:  # Bucle principal del juego
        system('clear')  # Limpia la pantalla
        tiempo = time.time()  # Inicializa el tiempo
        dificultad = menu()  # Muestra el menú y obtiene el nivel de dificultad seleccionado
        if dificultad == 0:  # Si el nivel de dificultad es 0, sale del juego
            break
        system('clear')  # Limpia la pantalla
        palabra_objetivo = generar_palabra(dificultad)  # Genera una palabra aleatoria
        numero_fallos = 0  # Inicializa el número de fallos
        letras_introducidas = []  # Inicializa la lista de letras introducidas
        colorear.printcolor('verde', 'BIENVENIDO AL JUEGO DEL AHORCADO','negrita')  # Muestra el mensaje de bienvenida Coloreado
        while True: # Bucle del juego
            mostrar_tiempo(tiempo)  # Muestra el tiempo transcurrido desde el inicio del juego
            ahorcado.dibujar_hombre(numero_fallos)  # Dibuja el ahorcado
            palabra_adivinada = construir_palabra_adivinada(palabra_objetivo,letras_introducidas)  # Construye la palabra a adivinar
            if '_' not in palabra_adivinada:  # Si no quedan guiones bajos en la palabra a adivinar, el jugador ha ganado
                system('clear')  # Limpia la pantalla
                colorear.printcolor('azul', '¡Felicidades! ¡Has ganado!', 'negrita','parpadeo')  # Muestra el mensaje de felicitación
                colorear.printcolor('verde', f'La palabra era: {palabra_objetivo}','negrita')  # Muestra la palabra a adivinar
                input()  # Espera a que el usuario pulse una tecla
                break  # Sale del bucle del juego
            if game_over(numero_fallos, palabra_objetivo, letras_introducidas):  # Si el juego ha terminado, el jugador ha perdido
                system('clear')  # Limpia la pantalla
                colorear.printcolor('rojo', f'Has perdido, la palabra era: {palabra_objetivo}', 'negrita','invertido')  # Muestra el mensaje de derrota
                input()  # Espera a que el usuario pulse una tecla
                system('clear')  # Limpia la pantalla
                horca.horca()  # Muestra la horca
                break  # Sale del bucle del juego
            get_nueva_letra(letras_introducidas)  # Obtiene una nueva letra introducida por el usuario
            numero_fallos += 1  # Incrementa el número de fallos
            system('clear')  # Limpia la pantalla
        continuar = input("¿Desea jugar de nuevo? (s/n): ")  # Pregunta al usuario si desea jugar de nuevo
        if continuar.lower() != "s":  # Si la respuesta no es 's', sale del bucle principal del juego
            break  # Sale del bucle principal del juego


if __name__ == '__main__':
    main()
