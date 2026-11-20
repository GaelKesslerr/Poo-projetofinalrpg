from modelos.personagens import Personagem


class Monstro(Personagem):
    def __init__(self, nome, nivel, vida, ataque, defesa, origem):
        super().__init__(nome, nivel, vida, ataque, defesa)
        self.origem = origem

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa

        if dano < 0:
            dano = 0

        return dano

    def habilidade_especial(self):
        return f"{self.nome} ameaça seus inimigos!"


class Golem(Monstro):
    def __init__(self, nome, nivel, vida, ataque, defesa, origem, resistencia):
        super().__init__(nome, nivel, vida, ataque, defesa, origem)
        self.resistencia = resistencia

    def habilidade_especial(self):
        return f"{self.nome} usa sua resistência para se proteger!"


class MortoVivo(Monstro):
    def __init__(self, nome, nivel, vida, ataque, defesa, origem, tipo_morte):
        super().__init__(nome, nivel, vida, ataque, defesa, origem)
        self.tipo_morte = tipo_morte

    def habilidade_especial(self):
        return f"{self.nome} usa seu poder de {self.tipo_morte}!"