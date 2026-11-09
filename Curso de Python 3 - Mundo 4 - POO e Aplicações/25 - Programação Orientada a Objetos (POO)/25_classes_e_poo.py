# Aula 25 - Programação Orientada a Objetos (POO)
# Guia de Classes, Instâncias, Encapsulamento, Herança e Polimorfismo

class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._ligado = False  # Atributo protegido

    def ligar(self):
        self._ligado = True
        print(f'{self.modelo} foi ligado.')

    def desligar(self):
        self._ligado = False
        print(f'{self.modelo} foi desligado.')

    def acelerar(self):
        if self._ligado:
            print(f'{self.modelo} está acelerando... Vrumm!')
        else:
            print(f'{self.modelo} não pode acelerar desligado.')

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, portas: int):
        super().__init__(marca, modelo, ano)
        self.portas = portas


class Moto(Veiculo):
    def acelerar(self):
        # Polimorfismo
        if self._ligado:
            print(f'Moto {self.modelo} acelerando em duas rodas... Randandandam!')
        else:
            print(f'Moto {self.modelo} desligada.')


if __name__ == '__main__':
    fusca = Carro('Volkswagen', 'Fusca 1300', 1974, 2)
    ninja = Moto('Kawasaki', 'Ninja 400', 2022)

    fusca.ligar()
    fusca.acelerar()

    ninja.ligar()
    ninja.acelerar()
