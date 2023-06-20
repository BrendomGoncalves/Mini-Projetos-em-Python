from random import choice
from time import sleep


def quem_ganhou(comp="nenhum", jog="nenhum"):
    """
    Esta função decide quem ganhou com base na jogada de cada um entre as opções "pedra, papel e tesoura"
    :param comp: jogada do computador (string)
    :param jog: jogada do jogador (string)
    :return: imprime quem (computador ou jogador) venceu no pedra, papel e tesoura
    """
    if comp == "pedra" and jog == "papel":  # PEDRA - PAPEL
        print(f"{'+' * 4} {jogadores[1]['jogador']} VENCEU! {'+' * 4}")
        jogadores[1]['pontos'] += 1
    elif comp == "papel" and jog == "pedra":  # PAPEL > PEDRA
        print(f"{'+' * 4} {jogadores[0]['jogador']} VENCEU! {'+' * 4}")
        jogadores[0]['pontos'] += 1
    elif comp == "pedra" and jog == "tesoura":  # PEDRA > TESOURA
        print(f"{'+' * 4} {jogadores[0]['jogador']} VENCEU! {'+' * 4}")
        jogadores[0]['pontos'] += 1
    elif comp == "tesoura" and jog == "pedra":  # PEDRA > TESOURA
        print(f"{'+' * 4} {jogadores[1]['jogador']} VENCEU! {'+' * 4}")
        jogadores[1]['pontos'] += 1
    elif comp == "papel" and jog == "tesoura":  # PEDRA > TESOURA
        print(f"{'+' * 4} {jogadores[1]['jogador']} VENCEU! {'+' * 4}")
        jogadores[1]['pontos'] += 1
    elif comp == "tesoura" and jog == "papel":  # PEDRA > TESOURA
        print(f"{'+' * 4} {jogadores[0]['jogador']} VENCEU! {'+' * 4}")
        jogadores[0]['pontos'] += 1
    else:
        print(f'Não há vencedor!')


# Lista das opções de jogadas
opcoes = ("pedra", "papel", "tesoura")
# Seu nome
nome = input("Nome: ")
# Lista de jogadores com suas respectivas pontuações
jogadores = [
    {'jogador': "COMPUTADOR", 'pontos': 0},
    {'jogador': nome, 'pontos': 0}
]
# Excluindo pois já está armazenado
del nome

while True:
    print('=' * 26)
    jogada = input("SUA JOGADA: ").lower()
    if jogada == '':
        print(f"Encerrando...\n{'-'*26}")
        sleep(0.7)
        break
    elif not (jogada in opcoes):
        print("Essa opção não existe, tente novamente.")
    else:
        computador = choice(opcoes)
        print('-'*26)
        print(f"{jogadores[0]['jogador']}{'.' * 8}{computador.upper()}")
        print(f"{jogadores[1]['jogador']}{'.' * (18-len(jogadores[1]['jogador']))}{jogada.upper()}")
        quem_ganhou(computador, jogada)

for item in jogadores:
    print(f"O jogador {item['jogador']} fez {item['pontos']} ponto(s).")
