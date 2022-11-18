import random

linhas = 6
colunas = 6
vet = [0] * colunas
vet_mapa = ["O"] * colunas
matriz = []
mapa = []
cont = 0
navio = 1
submarino = 2
porta_aviao = 3
cont_navio = 0
cont_sub = 0
cont_port = 0


def imprime(mat, L):
    cont = 0
    while cont > L:
        print(mat[cont])
        cont = cont + 1

def imprime_mapa(mat, L):
    cont = 0
    while cont < L:
        print(mat[cont])
        cont = cont + 1

while cont < linhas:
    matriz.append(vet.copy())
    mapa.append(vet_mapa.copy())
    print(matriz[cont])
    cont = cont + 1

while cont_navio < navio:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    matriz[lin][col] = 1
    cont_navio = cont_navio + 1

while cont_sub < submarino:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 1):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 2
    cont_sub = cont_sub + 1

while cont_port < porta_aviao:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 1) or (matriz[lin][col] == 2):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 3
    cont_port = cont_port + 1

print("-" * 15)
print("Batalha Naval!")
print("INSTRUÇÕES:")
print("1º O mapa do jogo tem tamanho 6x6, por isso escolha linhas e colunas entre 1 e 6")
print("2º  Você pode, em cada partida:")
print("- Ganhar 1 ponto, ao acertar um navio(N).")
print("- Ganhar 2 pontos, ao acertar um submarino(S).")
print("- Ganhar 3 pontos, ao acertar um porta-avião(P).")
print("-" * 15)


def jogo(linha, coluna):
    jog_01 = 0
    if matriz[linha - 1][coluna - 1] == 0:
        print("Você mirou na água!")
        matriz[lin_jog - 1][col_jog - 1] = "X"
        mapa[lin_jog - 1][col_jog - 1] = "X"
    elif matriz[linha - 1][coluna - 1] == 1:
        print("Você acertou um navio!")
        jog_01 = jog_01 + 1
        matriz[lin_jog - 1][col_jog - 1] = "N"
        mapa[lin_jog - 1][col_jog - 1] = "N"

    elif matriz[linha - 1][coluna - 1] == 2:
        print("Você acertou um submarino!")
        jog_01 = jog_01 + 2
        matriz[lin_jog - 1][col_jog - 1] = "S"
        mapa[lin_jog - 1][col_jog - 1] = "S"

    elif matriz[linha - 1][coluna - 1] == 3:
        print("Você acertou um porta-avião!")
        jog_01 = jog_01 + 3
        matriz[lin_jog - 1][col_jog - 1] = "P"
        mapa[lin_jog - 1][col_jog - 1] = "P"

    elif matriz[lin_jog - 1][col_jog - 1] == "X":
        print("Essa posição já foi bombardeada!")
        print("Aguarde a próxima jogada")
    elif matriz[lin_jog - 1][col_jog - 1] <= 0 and matriz[lin_jog - 1][col_jog - 1] >= 7:
        print("Essa posição não existe no mapa! Digite um número entre 1 e 6!")
        print("Perdeu a vez!")
    else:
        jog_01 = jog_01 + 0
    return (jog_01)


while True:
    jogadores = int(input("Quantos jogadores participarão da batalha?"))
    if jogadores > 0 and jogadores < 4:
        break
    else:
        print("-" * 30)
        print("**Escolha um número de jogadores válido!**")
        print("-" * 30)

print("-" * 30)
print("O jogo começou!")
print("-" * 30)

p_jog01 = 0
p_jog02 = 0
p_jog03 = 0
cont_navio = 3
cont_sub = 2
cont_port = 3

while True:
    print("")
    print("Jogador 01")
    imprime_mapa(mapa, linhas)
    col_jog = int(input("Qual a coluna? "))
    lin_jog = int(input("Qual a linha? "))
    print("-" * 30)
    jogador01 = int(jogo(lin_jog, col_jog))
    matriz[lin_jog - 1][col_jog - 1] = "X"
    p_jog01 = p_jog01 + jogador01
    if jogador01 == 1:
        cont_navio = cont_navio - 1
    if jogador01 == 2:
        cont_sub -= 1
    if jogador01 == 3:
        cont_port -= 1
    print("o jogador 01 tem {} pontos".format(p_jog01))
    print("")
    print("-" * 30)
    if jogadores == 2:
        print("")
        print("Jogador 02")
        imprime_mapa(mapa, linhas)
        col_jog = int(input("Qual a coluna? "))
        lin_jog = int(input("Qual a linha? "))
        print("-" * 30)
        jogador02 = int(jogo(lin_jog, col_jog))
        matriz[lin_jog - 1][col_jog - 1] = "X"
        p_jog02 = p_jog02 + jogador02
        if jogador02 == 1:
            cont_navio = cont_navio - 1
        if jogador02 == 2:
            cont_sub -= 1
        if jogador02 == 3:
            cont_port -= 1
        print("o jogador 02 tem {} pontos".format(p_jog02))
        print("")
        print("-" * 30)
    if jogadores == 3:
        print("")
        print("Jogador 02")
        imprime_mapa(mapa, linhas)
        col_jog = int(input("Qual a coluna? "))
        lin_jog = int(input("Qual a linha? "))
        print("-" * 30)
        jogador02 = int(jogo(lin_jog, col_jog))
        matriz[lin_jog - 1][col_jog - 1] = "X"
        p_jog02 = p_jog02 + jogador02
        if jogador02 == 1:
            cont_navio = cont_navio - 1
        if jogador02 == 2:
            cont_sub -= 1
        if jogador02 == 3:
            cont_port -= 1
        print("o jogador 02 tem {} pontos".format(p_jog02))
        print("")
        print("-" * 30)
        print("")
        print("Jogador 03")
        imprime_mapa(mapa, linhas)
        col_jog = int(input("Qual a coluna? "))
        lin_jog = int(input("Qual a linha? "))
        print("-" * 30)
        jogador03 = int(jogo(lin_jog, col_jog))
        matriz[lin_jog - 1][col_jog - 1] = "X"
        p_jog03 = p_jog03 + jogador03
        if jogador03 == 1:
            cont_navio = cont_navio - 1
        if jogador03 == 2:
            cont_sub -= 1
        if jogador03 == 3:
            cont_port -= 1
        print("o jogador 03 tem {} pontos".format(p_jog03))
        print("")
        print("-" * 30)
    print("Navio {}".format(cont_navio))
    print("Porta Avião {}".format(cont_port))
    print("Submarino {}".format(cont_sub))
    if jogadores == 2 and p_jog01 + p_jog02 == 14:
        break
    if jogadores == 3 and p_jog01 + p_jog02 + p_jog03 == 14:
        break
if jogadores == 2:
    if p_jog01 == p_jog02:
        print("EMPATE")
    elif (p_jog01 > p_jog02):
        print("JOGADOR 01 VENCEU!")
    else:
        print("JOGADOR 02 VENCEU!")

if jogadores == 3:
    if p_jog01 == p_jog02 and p_jog03 < p_jog01:
        print("EMPATE DE JOGADOR 01 E 02 ")
    if p_jog03 == p_jog02 and p_jog01 < p_jog02:
        print("EMPATE DE JOGADOR 02 E 03 ")
    if p_jog03 == p_jog01 and p_jog02 < p_jog03:
        print("EMPATE DE JOGADOR 01 E 03 ")
    elif (p_jog01 > p_jog02):
        if (p_jog01 > p_jog03):  # 1>2/3
            print("JOGADOR 01 VENCEU!")
        if (p_jog01 < p_jog03):  # 3>1/2
            print("JOGADOR 03 VENCEU!")

    elif (p_jog02 > p_jog01):
        if (p_jog02 > p_jog03):  # 2>1/3
            print("JOGADOR 02 VENCEU!")
        if (p_jog02 < p_jog03):  # 3>1/2
            print("JOGADOR 03 VENCEU!")

    elif (p_jog02 > p_jog01):
        if (p_jog02 < p_jog03):  # 3>2/1
            print("JOGADOR 03 VENCEU!")
        if (p_jog02 > p_jog03):  # 2>2/3
            print("JOGADOR 02 VENCEU!")