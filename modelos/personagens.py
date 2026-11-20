from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome, nivel, vida, ataque, defesa):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def habilidade_especial(self):
        pass

    def __str__(self):
        return f"{self.nome} - Nível {self.nivel} - Vida: {self.vida}"