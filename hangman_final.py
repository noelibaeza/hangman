import random
import os
# cantidad de vidas iniciales
initial_lifes = 7

# agregar los países a una lista países
paises = ["QATAR", "ALEMANIA",	"DINAMARCA", "BELGICA", "FRANCIA", "CROACIA", "ESPAÑA", "SERBIA", "INGLATERRA", "SUIZA", "PAISES BAJOS", "BRASIL", "ARGENTINA", "IRAN", "COREA DEL SUR", "URUGUAY",
          "ECUADOR", "JAPON", "ARABIA SAUDITA", "PORTUGAL", "POLONIA", "SENEGAL", "GHANA", "MARRUECOS", "TUNEZ", "CAMERUN", "CANADA" "MEXICO", "ESTADOS UNIDOS", "GALES", "AUSTRALIA", "COSTA RICA"]

# seleccionar uno de los países de forma aleatoria y generar cadena de guiones bajo que tenga tantos guiones bajo como la cadena original


def crearCadenas():
    pais = random.choice(paises)  # elijo un pais al azar en la lista de paises
    # agrego un guion bajo por cada simbolo en la palabra del pais
    secreto = '_'*len(pais)
    return pais, secreto


def trofeosRestantes(message, cantidad):
    print(message + ("🏆" * cantidad) + '\n')


# cadena original donde quiero buscar el simbolo, cadena secreto y nuestro simbolo
def reemplazarSimbolo(original, secreto, simbolo):
    # primero hay que contar cuantas veces aparece el simbolo en la cadena original
    cantidad = original.count(simbolo)
    inicio = 0  # posicion de inicio
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos]+simbolo+secreto[pos+1:]
        inicio = pos+1
    return secreto


def limpiarPantalla():
    # posix is os name for Linux or mac
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')


def ahorcado():
    nom = input("Ingrese su nombre 👩🧑: ")
    while nom == '':
        print('Debe ingresar su nombre :(')
        nom = input("Ingrese su nombre: ")
    limpiarPantalla()
    mensaje = "\nBienvenido/a " + nom + \
        ", vamos a jugar al juego del ahorcado.La palabra secreta a adivinar será uno de los paises clasificados para el mundial de fútbol Qatar 2022. Tienes 7 vidas disponibles. Ten en cuenta que los espacios en blanco también cuentan como caracter a ingresar. Good Lock!! 🎇🎉\n"
    print(mensaje)
    input('Presiona enter para comenzar ')
    original, secreto = crearCadenas()
    burned_lifes = 0
    letras_erradas = ''
    while secreto != original and burned_lifes < initial_lifes:
        # limpiar pantalla y muestra trofeos
        limpiarPantalla()
        trofeosRestantes("Te quedan: ", initial_lifes - burned_lifes)
        if(letras_erradas != ''):
            print("Letras erradas:" + letras_erradas + '\n')
        print(f'Palabra:{secreto} \n')
        s = input('Ingresa una letra: ')
        # Verificar que se ingrese una letra
        if(s != '' and len(s) == 1):
            s = s.upper()
            if s in original:
                secreto = reemplazarSimbolo(original, secreto, s)
                print('¡Muy bien!\n')
            else:
                print('Lo siento, la letra no pertenece a la palabra.\n')
                letras_erradas += ' ' + s
                burned_lifes += 1
        else:
            print('Debe ingresar una única letra válida.\n')
        input('Presiona enter para continuar... ')
    if secreto == original:
        limpiarPantalla()
        print(f'¡🏆Felicidades el país es {secreto}!\n')
        trofeosRestantes("Ganaste: ", initial_lifes - burned_lifes)
    else:
        limpiarPantalla()
        print(f'Lo siento 💔, el país era {original}\n')
        print('Intenta nuevamente')


ahorcado()
