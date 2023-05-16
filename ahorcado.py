"""
.. include:: ./README.md
"""

import random


class juegoAhorcado:
    """
    Esta clase implementa un juego del ahorcado donde hay 3 categorias diferentes y tiene que adivinar
    la letra de una palabra.
    - **categoria**: lista de diferentes categorias.
    - **estados**: los estados del ahorcado.
    - **salvado**: el estado salvado del ahorcado.
    - **lista_frutas**: lista de las frutaas.
    - **lista_animales**: lista de animales.
    - **lista_colores**: lista de colores.
    """
    ESTADOS = [
        r"""
         +--+
         |  |
            |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
         |  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        /   |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        / \ |
            |
        ====="""]

    SALVADO = [
        r"""
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""]
    categoria = ['FRUTA', 'ANIMALES', 'COLORES']
    lista_frutas = ['PERA', 'PLATANO', 'UVA', 'MANZANA', 'MELOCOTON', 'KIWI', 'ALBARICOQUE', 'CEREZA', 'CIRUELA',
                    'FRESA', 'GRANADA', 'HIGO', 'LIMA', 'LIMON', 'MANDARINA', 'NARANJA', 'MELON', 'MORA', 'NISPERO',
                    'PIÑA', 'POMELO', 'SANDIA']

    lista_animales = ['LEON', 'TIGRE', 'ELEFANTE', 'JIRAFA', 'CANGURO']
    lista_colores = ['ROJO', 'VERDE', 'AZUL', 'AMARILLO', 'NARANJA']

    palabra_secreta = random.choice(lista_frutas)

    cat_seleccionada = random.choice(categoria)

    def jugar(self):
        """
        Método que inicializa el juego, selecciona la categoría aleatoriamente y si la letra introducida se encuentra
        en la palabra secreta se guarda en la lista de letras_correctas si no en la lista de incorrectas. Cuando la
        lista de letras_incorrectas es igual muñeco colgado (número de intentos), para el bucle y muestra la palabra
        secreta. Si la nueva letra es 'TERMINAR' se acaba el juego y muestra el muñeco colgado y la solución.

        """
        letras_incorrectas = []
        letras_correctas = []
        palabra_secreta = ""

        if self.cat_seleccionada == "FRUTA":
            palabra_secreta = random.choice(self.lista_frutas)
        elif self.cat_seleccionada == "ANIMALES":
            palabra_secreta = random.choice(self.lista_animales)
        elif self.cat_seleccionada == "COLORES":
            palabra_secreta = random.choice(self.lista_colores)

        nombre = input("Introduce tu nombre: ")
        while True:

            self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)

            nueva_letra = self.introduce_letra(letras_incorrectas + letras_correctas)

            if nueva_letra == "TERMINAR":
                print(self.ESTADOS[-1])
                print("La palabra era: " + palabra_secreta)
                break

            if nueva_letra in palabra_secreta:

                letras_correctas.append(nueva_letra)

                ganar = True
                for letra_secreta in palabra_secreta:
                    if letra_secreta not in letras_correctas:
                        ganar = False
                        break
                if ganar:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', palabra_secreta)
                    print(f'Has ganado, {nombre}!')
                    break

            else:
                letras_incorrectas.append(nueva_letra)

                if len(letras_incorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabra_secreta))
                    break

    def dibujar(self, letras_incorrectas, letras_correctas, secreto):
        """
        Método que dibuja el ahorcado sin colgar y según vas fallando las letras se va dibujando el colgado del muñeco.
        Se muestra el número de intentos cada vez que fallas y si aciertas se pone la letra correcta en los espacios
        de la palabra secreta.


        :param letras_incorrectas: char
        :param letras_correctas: char
        :param secreto: String

        """
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es: ', self.cat_seleccionada)
        print()
        print()

        intentos_restantes = self.obtener_intentos_restantes(letras_incorrectas)
        print(f"Te quedan {intentos_restantes} intentos antes de perder la partida.")

        print('Letras incorrectas: ', end='')

        for letra in letras_incorrectas:
            print(letra, end=' ')
        if len(letras_incorrectas) == 0:
            print('No hay letras incorrectas.')
        if len(letras_incorrectas) == len(letras_correctas) + 1:
            print('Letras diferentes.')
        if len(letras_incorrectas) == len(letras_correctas) + 2:
            print('No coinciden.')

        print()

        espacio = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in letras_correctas:
                espacio[i] = secreto[i]

        print(' '.join(espacio))

    @staticmethod
    def introduce_letra(fletra):
        """
        Metodo que se le pasa un carácter que en el metodo de jugar() se le pasa como la combinacion de la lisa de
        letras_correctas + letras_incorrectas. Después pide al usuario introducir una letra y realiza las
        comprobaciones, si es correcto devuelve de la letra introducida. Si el usario pone TERMINAR se devuelve la
        String de TERMINAR.

        :param fletra: Char
        :return: adivina
        """
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if adivina == "TERMINAR":
                return adivina
            elif len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in fletra:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')
            else:
                return adivina

    def obtener_intentos_restantes(self, letras_incorrectas):
        """
        Metodo que devuelve el número de intentos restantes.

        :param letras_incorrectas:
        :return: Int: número de intentos.
        """
        return len(self.ESTADOS) - 1 - len(letras_incorrectas)


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
