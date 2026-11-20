from modelos.personagens import Personagem
from modelos.herois import Guerreiro, Mago, Arqueiro
from modelos.monstros import Golem, MortoVivo


# Criando os herois
guerreiro = Guerreiro("Arthas", 5, 120, 30, 15, "Lordaeron", "Espada")

mago = Mago("Merlin", 4, 80, 35, 8, "Avalon", 100)

arqueiro = Arqueiro("Legolas", 5, 90, 25, 10, "Floresta", 40)


# Criando os monstros
golem = Golem("Pedregulho", 3, 150, 20, 25, "Montanhas", 50)

morto_vivo = MortoVivo("Zumbi", 2, 70, 18, 5, "Cemitério", "morte sombria")

# Lista com todos os personagens
personagens = [guerreiro, mago, arqueiro, golem, morto_vivo]

for personagem in personagens:
    print(personagem)
    print(personagem.habilidade_especial())
    print("--------------------------")


# Verificando a herança
print(isinstance(guerreiro, Personagem))
print(isinstance(golem, Personagem))