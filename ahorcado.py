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

    lista_frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE ' \
        'CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA ' \
        'NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        letras_incorrectas = []
        letras_correctas = []
        palabra_secreta = random.choice(self.lista_frutas)

        nombre = input("Introduce tu nombre: ")
        while True:

            self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)

            nueva_letra = self.introduce_letra(letras_incorrectas + letras_correctas)

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
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es: FRUTAS')
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
            if len(adivina) != 1:
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
