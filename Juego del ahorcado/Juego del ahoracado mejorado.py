import os, random, sys
from colorama import Fore, Style, init
init(autoreset=True)

# -------- Función para leer una tecla --------
def getch():
    if os.name == 'posix':
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    else:
        import msvcrt
        sys.stdout.flush()
        return msvcrt.getwch()

# -------- Diccionario de palabras y pistas --------
palabras_y_pistas = {
    "Motosierra": "Herramienta que sirve para cortar madera.",
    "Botella": "Se utiliza para almacenar líquidos.",
    "Palo": "Objeto largo, delgado y de madera.",
    "Telefono": "Sirve para realizar llamadas."
}

# -------- Variables iniciales --------
palabra = random.choice(list(palabras_y_pistas.keys()))
pista = palabras_y_pistas[palabra]
oportunidades = 6
n = len(palabra)
turnos = 0
aciertos = 0
casillas = ['_'] * n

# -------- Figuras del ahorcado --------
def mostrar_ahorcado(turnos):
    figuras = [
        """
         ------
         |    |
              |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
         X    |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /X    |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /X|   |
              |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /X|   |
        /     |
              |
        =========
        """,
        """
         ------
         |    |
         O    |
        /X|   |
        / |   |
              |
        =========
        """
    ]
    print(Fore.YELLOW + figuras[turnos])

# -------- Juego --------
print(Fore.CYAN + "¡Bienvenido al juego del Ahorcado!\n")
print(Fore.GREEN + f"Pista: {pista}\n")

while turnos < oportunidades and aciertos < n:
    print(Fore.MAGENTA + f"Oportunidades restantes: {oportunidades - turnos}")
    mostrar_ahorcado(turnos)

    for c in casillas:
        sys.stdout.write(Fore.WHITE + ' ' + c)
    print()

    print(Fore.CYAN + "\nEscribe una letra: ", end='')
    letra = getch()
    print(Fore.WHITE + letra)

    encontrado = False
    for i in range(n):
        caracter = palabra[i]
        if letra.upper() == caracter.upper():
            encontrado = True
            if casillas[i] == '_':
                casillas[i] = caracter
                aciertos += 1

    if not encontrado:
        turnos += 1
        print(Fore.RED + 'Letra no encontrada.')

# -------- Resultado --------
mostrar_ahorcado(turnos)
if aciertos == n:
    print(Fore.GREEN + "\n🎉 ¡Felicidades, has ganado!")
else:
    print(Fore.RED + "\n😢 Has perdido.")
print(Fore.YELLOW + f"La palabra secreta era: {palabra}")
