import random

# INICIO DO JOGO
def iniciar():
    print('x=x=x=x=x=x=x=x=x=x=x=x=x=x=x\n|          DEEP SEA         |\nx=x=x=x=x=x=x=x=x=x=x=x=x=x=x')

    # CONFIGURAÇÃO PRINCIPAL
    # MAPA
    profundidade = obter_mapa()
    oxigenio_inicial = obter_oxigenio()

    # JOGADORES

    num_jogadores = obter_num_jogadores()
    jogadores = inicializar_jogadores(num_jogadores, oxigenio_inicial)

    # TURNO

    for turno in range(1, 11):
        print(f'Turno: {turno}')
        for jogador in jogadores:
            começar_turno(jogador, profunidade)
    
    # VENCEDOR

    vencedor = obter_vencedor(jogadores):
    print(f'O jogador {vencedor['nome']} venceu com {vencedor['pontos']} pontos!')

def escolha_mapa():
    while True:
        mapa = int(input(('Escolha o tamanho do mapa (15, 30 ou 45 metros): ')))
        if mapa in [15, 30, 45]:
            return mapa
        else:
            print('Opção incorreta! Escolha entre 15, 30 ou 45 metros!')

def escolha_oxigenio():
    while True:
        oxigenio = int(input('Escolha a quantidade inicial de oxigênio (Entre 45 e 120): '))
        if 45 <= oxigenio <= 120:
            return oxigenio
        else:
            print('Opção incorreta! Escolha entre 45 e 120!')

def quantidade_jogadores():
    while True:
        num_jogadores = int(input('Digite o número de jogadores (Entre 4 e 6): '))
        if 4 <= num_jogadores <= 6:
            return num_jogadores
        else:
            print('Opção incorreta! Digite entre 4 e 6')

def selecionar_jogador(num_jogadores, oxigenio_inicial):
    jogadores = []
    for n in range(1, num_jogadores, 1):
        nome = input(f'Nome do jogador: {n}')
        jogadores.append({
            'nome:': nome,
            'posição': 0,
            'tesouros': [],
            'oxigenio': oxigenio_inicial
        })
    return jogadores





