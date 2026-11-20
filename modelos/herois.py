from modelos.personagens import Personagem
from modelos.interfaces import Curavel, Equipavel


class Heroi(Personagem, Curavel):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino):
        super().__init__(nome, nivel, vida, ataque, defesa)
        self.reino = reino

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa

        if dano < 0:
            dano = 0

        return dano

    def habilidade_especial(self):
        return f"{self.nome} luta pelo reino de {self.reino}!"

    def receber_cura(self, quantidade):
        self.vida += quantidade
        return f"{self.nome} recuperou {quantidade} pontos de vida!"


class Guerreiro(Heroi, Equipavel):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, arma):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.arma = arma

    def atacar(self, alvo):
        dano = super().atacar(alvo) + 10
        return dano

    def habilidade_especial(self):
        return f"{self.nome} utiliza {self.arma} para executar um golpe poderoso!"

    def equipar(self, arma):
        self.arma = arma
        return f"{self.nome} equipou {arma}!"

    def desequipar(self):
        arma = self.arma
        self.arma = None
        return f"{self.nome} desequipou {arma}."

    def __str__(self):
        return super().__str__() + f" - Guerreiro armado com {self.arma}"


class Mago(Heroi):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, mana):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.mana = mana

    def habilidade_especial(self):
        return f"{self.nome} usa magia com seus {self.mana} pontos de mana!"


class Arqueiro(Heroi, Equipavel):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, chance_critico):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.chance_critico = chance_critico
        self.arma = "Arco e flecha"

    def habilidade_especial(self):
        return f"{self.nome} prepara uma flecha com {self.chance_critico}% de chance de crítico!"

    def equipar(self, arma):
        self.arma = arma
        return f"{self.nome} equipou {arma}!"

    def desequipar(self):
        arma = self.arma
        self.arma = None
        return f"{self.nome} desequipou {arma}."