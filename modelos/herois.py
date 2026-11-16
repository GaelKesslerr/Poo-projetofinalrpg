from modelos.personagem import Personagem


# Classe
class Heroi(Personagem):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino):
        super().__init__(nome, nivel, vida, ataque, defesa)
        self.reino = reino

    # Habilidade geral dos herois
    def habilidade_especial(self):
        return f"{self.nome} luta pelo reino de {self.reino}!"


# Guerreiro
class Guerreiro(Heroi):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, arma):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.arma = arma

    # Aumenta o dano do ataque usando o metodo da classe anterior
    def atacar(self, alvo):
        dano = super().atacar(alvo) + 10
        return dano

    def habilidade_especial(self):
        return f"{self.nome} utiliza {self.arma} para executar um golpe poderoso!"


    def __str__(self):
        return super().__str__() + f" - Guerreiro armado com {self.arma}"


# Mago
class Mago(Heroi):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, mana):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.mana = mana

    def habilidade_especial(self):
        return f"{self.nome} usa magia com seus {self.mana} pontos de mana!"


# Arqueiro
class Arqueiro(Heroi):
    def __init__(self, nome, nivel, vida, ataque, defesa, reino, chance_critico):
        super().__init__(nome, nivel, vida, ataque, defesa, reino)
        self.chance_critico = chance_critico

    def habilidade_especial(self):
        return f"{self.nome} prepara uma flecha com {self.chance_critico}% de chance de critico!"