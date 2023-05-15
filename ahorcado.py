import random


class juegoAhorcado:
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
    lista_frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE ' \
        'CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA ' \
        'NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    lista_animales = ['LEON', 'TIGRE', 'ELEFANTE', 'JIRAFA', 'CANGURO']
    lista_colores = ['ROJO', 'VERDE', 'AZUL', 'AMARILLO', 'NARANJA']

    palabra_secreta = random.choice(lista_frutas)

    cat_seleccionada = random.choice(categoria)

    def jugar(self):

        letras_incorrectas = []
        letras_correctas = []
        palabra_secreta = ""

        if self.cat_seleccionada == "FRUTAS":
            palabra_secreta = random.choice(self.lista_frutas)
        elif self.cat_seleccionada == "ANIMALES":
            palabra_secreta = random.choice(self.lista_animales)
        elif self.cat_seleccionada == "COLORES":
            palabra_secreta = random.choice(self.lista_colores)

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
                    print('Has ganado!')
                    break

            else:
                letras_incorrectas.append(nueva_letra)

                if len(letras_incorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabra_secreta))
                    break

    def dibujar(self, letras_incorrectas, letras_correctas, secreto):
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es: ', self.cat_seleccionada)
        print()

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


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
