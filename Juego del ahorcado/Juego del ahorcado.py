import os, random, sys

def getch ():
    if os.name == 'posix':
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw (sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr (fd, termios.TCSADRAIN, old_settings)
        return ch
    else:
        import msvcrt, sys
        sys.stdout.flush()
        return msvcrt.getwch()

oportunidades = 6
palabras = [
    'Motosierra',
    'Botella',
    'palo',
    'telefono'
]
palabra = random.choice(palabras)
n = len (palabra)
turnos = 0
aciertos = 0
cabeza = ' '
cuerpo = ' '
manoIzquierda = ' '
manoDerecha = ' '
pieIzquierdo = ' '
pieDerecho = ' '
casillas = []
for i in range (n):
    casillas.append ('_')
while turnos < oportunidades and aciertos < n:
    print ('\nOportunidades restantes: ' + repr (oportunidades - turnos))
    for i in range (n):
        sys.stdout.write (' ' + casillas[i])
    sys.stdout.write ('\nEscriba una letra: ')
    letra = getch()
    print (letra)
    encontrado = False
    for i in range (n):
        caracter = palabra[i]
        if letra.upper() == caracter.upper():
            encontrado = True
            if casillas[i] == '_':
                casillas[i] = caracter
                aciertos += 1
    if not encontrado:
        turnos += 1
        print ('Letra no encontrada.')
        if turnos==1:
            cabeza = 'O'
        elif turnos==2:
            cuerpo = 'X'
        elif turnos==3:
            manoDerecha = '/'
        elif turnos==4:
            manoIzquierda = '|'
        elif turnos==5:
            pieDerecho = '/'
        elif turnos==6:
            pieIzquierdo = '|'
    print ('     ' + cabeza + ' ')
    print ('    ' + manoDerecha + cuerpo + manoIzquierda)
    print ('    ' + pieDerecho + ' ' + pieIzquierdo + '\n')
if aciertos==n:
    print ('Felicidades, has ganado.')
else:
    print ('Has perdido.')
print ('La palabra secreta es: ' + palabra)