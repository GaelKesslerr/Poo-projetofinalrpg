class Personagem:
    def __init__(self, nome, nivel, vida, ataque, defesa):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa

        if dano < 0:
            dano = 0

        return dano

    def habilidade_especial(self):
        return "Este personagem não possui habilidade especial."

    def __str__(self):
        return f"{self.nome} - Nível {self.nivel} - Vida: {self.vida}"