import random

# Função para criar o tabuleiro vazio
def criar_tabuleiro(linhas, colunas):
    tabuleiro = []
    for _ in range(linhas):
        linha = [' '] * colunas
        tabuleiro.append(linha)
    return tabuleiro

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    print('   ' + '  '.join([str(i) for i in range(colunas)]))
    print('  ' + '---' * colunas)

    for i in range(linhas):
        print(str(i) + ' |' + ' |'.join(tabuleiro[i]) + ' |')
        print('  ' + '---' * colunas)

# Função para colocar as minas no tabuleiro
def colocar_minas(tabuleiro, minas):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    minas_colocadas = 0

    while minas_colocadas < minas:
        x = random.randint(0, colunas - 1)
        y = random.randint(0, linhas - 1)

        if tabuleiro[y][x] != '*':
            tabuleiro[y][x] = '*'
            minas_colocadas += 1

# Função para verificar se uma coordenada é válida
def coordenada_valida(x, y, tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    if x < 0 or x >= colunas:
        return False
    if y < 0 or y >= linhas:
        return False

    return True

# Função para contar o número de minas adjacentes a uma coordenada
def contar_minas_adjacentes(x, y, tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if coordenada_valida(x + j, y + i, tabuleiro) and tabuleiro[y + i][x + j] == '*':
                count += 1

    return count

# Função para revelar uma célula
def revelar_celula(x, y, tabuleiro, tabuleiro_visivel):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    if not coordenada_valida(x, y, tabuleiro):
        return

    if tabuleiro_visivel[y][x] != ' ':
        return

    if tabuleiro[y][x] == '*':
        tabuleiro_visivel[y][x] = '*'
        return

    minas_adjacentes = contar_minas_adjacentes(x, y, tabuleiro)
    tabuleiro_visivel[y][x] = str(minas_adjacentes)

    if minas_adjacentes == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                revelar_celula(x + j, y + i, tabuleiro, tabuleiro_visivel)

# Função principal do jogo
def jogar_campo_minado(linhas, colunas, minas):
    tabuleiro = criar_tabuleiro(linhas, colunas)
    tabuleiro_visivel = criar_tabuleiro(linhas, colunas)

    colocar_minas(tabuleiro, minas)

    jogo_terminado = False

    while not jogo_terminado:
        imprimir_tabuleiro(tabuleiro_visivel)

        x = int(input('Digite a coordenada x: '))
        y = int(input('Digite a coordenada y: '))

        if not coordenada_valida(x, y, tabuleiro_visivel):
            print('Coordenadas inválidas. Tente novamente.')
            continue

        if tabuleiro_visivel[y][x] != ' ':
            print('Essa célula já foi revelada. Tente novamente.')
            continue

        revelar_celula(x, y, tabuleiro, tabuleiro_visivel)

        if tabuleiro[y][x] == '*':
            print('Você perdeu! Tente novamente.')
            jogo_terminado = True
        elif all(' ' not in linha for linha in tabuleiro_visivel):
            print('Você ganhou! Parabéns!')
            jogo_terminado = True

# Execução do jogo
jogar_campo_minado(10, 10, 10)
