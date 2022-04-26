# ====================
# FUNÇÕES
# ====================
# Cria o tabuleiro inical limpo e o exibe
def tabuleiro_inicial():
    linha_tabuleiro = []
    for i in range(tabuleiro):
        for j in range(tabuleiro):
            linha_tabuleiro.extend([0])
        tabuleiro_montado.extend([linha_tabuleiro])
        linha_tabuleiro = []

# Exibe o tabuleiro
def exibe_tabuleiro():
    for i in range(tabuleiro):
        for j in range(tabuleiro):
            print(str(tabuleiro_montado[i][j]) + " ", end='')
        print("\n", end='')

# Efetua a jogada
def jogada(joga_id, joga_linha, joga_coluna):
    # Verifica se o ID está correto
    joga_id = valida_id(str(joga_id), 1)

    # Verifica se o campo está dentro dos limites
    while (joga_linha < 0) or (joga_linha > tabuleiro) or (joga_coluna < 0) or (joga_coluna > tabuleiro):
        nova_jogada = input("\nCampo fora dos limites!\nPor favor, digite novamente a linha e coluna separada por espaço: ").split(' ')
        joga_linha = int(nova_jogada[0])
        joga_coluna = int(nova_jogada[1])
    
    # Verifica se o campo já está ocupado
    while tabuleiro_montado[joga_linha - 1][joga_coluna - 1] != 0:
        nova_jogada = input("\nCampo já ocupado!\nPor favor, digite novamente a linha e coluna separada por espaço: ").split(' ')
        joga_linha = int(nova_jogada[0])
        joga_coluna = int(nova_jogada[1])
        # Verifica se o campo está dentro dos limites
        while (joga_linha < 0) or (joga_linha > tabuleiro) or (joga_coluna < 0) or (joga_coluna > tabuleiro):
            nova_jogada = input("\nCampo fora dos limites!\nPor favor, digite novamente a linha e coluna separada por espaço: ").split(' ')
            joga_linha = int(nova_jogada[0])
            joga_coluna = int(nova_jogada[1])        
    
    # Altera o tabuleiro
    tabuleiro_montado[joga_linha-1][joga_coluna-1] = joga_id

    # Pega o nome do jogador para registrar a jogada
    for i in range(jogadores):
        if(lista_jogador[i][1] == joga_id):
            nome_jogada = str(lista_jogador[i][0])

    # Registra a jogada no arquivo
    arquivo = open(nome_arquivo+".txt", "a") # Abre o arquivo
    arquivo.writelines(nome_jogada + " jogou em " + str(joga_linha) + " " + str(joga_coluna) + "\n") # Registra a informação
    arquivo.close() # Fecha o arquivo

    # Chama a verificação de fim de jogo
    fim_jogo(joga_id, joga_linha-1, joga_coluna-1)

# Verifica se o jogo acabou a partir da última jogada para não ter que rodar todo o tabuleiro
def fim_jogo(ultimo_id, ultima_linha, ultima_coluna):
    vencedor = 0 # Para verificar se o jogo foi finalizado. 0 -> Não; 1 -> Sim
    empate = 1 # Para verificar se o jogo empatou. 0 -> Não; 1 -> Sim
    
    # Verifica linha genérico
    if ultima_coluna == 0: # Primeira coluna
        # 2 campos para frente
        if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+2] == ultimo_id):
            vencedor = 1
    elif ultima_coluna == tabuleiro-1: # Última coluna
        # 2 campos para trás
        if(tabuleiro_montado[ultima_linha][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
            vencedor = 1

    # Verifica coluna genérico
    if ultima_linha == 0: # Primeira linha
        # 2 campos para baixo
        if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna] == ultimo_id):
            vencedor = 1
    elif ultima_linha == tabuleiro-1: # Última linha
        # 2 campos para cima
        if(tabuleiro_montado[ultima_linha-2][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
            vencedor = 1

    # Verifica diagonal \ (esquerda -> direita)
    if(ultima_linha == 0) and (ultima_coluna == 0): # Posição 0,0
        # 2 campos diagonal \ baixo
        if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna+2] == ultimo_id):
            vencedor = 1
    elif(ultima_linha == 0) and (ultima_coluna == 0): # Posição N,N
        # 2 campos diagonal \ cima
        if(tabuleiro_montado[ultima_linha-2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
            vencedor = 1

    # Verifica diagonal / (direita -> esquerda)
    if(ultima_linha == 0) and (ultima_coluna == 0): # Posição 0,N
        # 2 campos diagonal / baixo
        if(tabuleiro_montado[ultima_linha+2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
            vencedor = 1
    elif(ultima_linha == 0) and (ultima_coluna == 0): # Posição N,0
        # 2 campos diagonal / cima
        if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha-2][ultima_coluna+2] == ultimo_id):
            vencedor = 1
            
    if tabuleiro > 3: # Para verificar campos atrás e frente sem sair dos limites do tabuleiro
        # Linha
        if ultima_coluna == 1:
            # 2 campos para frente
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 1 trás + 1 frente
            elif(tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id):
                vencedor = 1
        elif ultima_coluna == tabuleiro-2:
            # 2 campos para trás
            if(tabuleiro_montado[ultima_linha][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 trás + 1 frente
            elif(tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id):
                vencedor = 1
        else:
            # 2 campos para frente
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 2 campos para trás
            elif(tabuleiro_montado[ultima_linha][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 trás + 1 frente
            elif(tabuleiro_montado[ultima_linha][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna+1] == ultimo_id):
                vencedor = 1

        # Coluna
        if ultima_linha == 1:
            # 2 campos para baixo
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 cima + 1 baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id):
                vencedor = 1
        elif ultima_linha == tabuleiro-2:
            # 2 campos para cima
            if(tabuleiro_montado[ultima_linha-2][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 cima + 1 baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id):
                vencedor = 1
        else:
            # 2 campos para baixo
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 2 campos para cima
            elif(tabuleiro_montado[ultima_linha-2][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 cima + 1 baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna] == ultimo_id):
                vencedor = 1

        # Diagonal \ (esquerda -> direita)
        if (ultima_linha == 1) and (ultima_coluna == 1):
            # 2 campos diagonal \ baixo
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 1 diagonal \ cima + 1 diagonal \ baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id):
                vencedor = 1
        elif (ultima_linha == tabuleiro-2) and (ultima_coluna == tabuleiro-2):
            # 2 campos diagonal \ cima
            if(tabuleiro_montado[ultima_linha-2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 diagonal \ cima + 1 diagonal \ baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id):
                vencedor = 1
        else:
            # 2 campos diagonal \ baixo
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha+2][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 2 campos diagonal \ cima
            elif(tabuleiro_montado[ultima_linha-2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 diagonal \ cima + 1 diagonal \ baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna+1] == ultimo_id):
                vencedor = 1

        # Diagonal / (direita -> esquerda)
        if (ultima_linha == 1) and (ultima_coluna == tabuleiro-2):
            # 2 campos diagonal / baixo
            if(tabuleiro_montado[ultima_linha+2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 1 diagonal / cima + 1 diagonal / baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id):
                vencedor = 1
        elif (ultima_linha == tabuleiro-2) and (ultima_coluna == 1):
            # 2 campos diagonal / cima
            if(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha-2][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 1 diagonal / cima + 1 diagonal / baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id):
                vencedor = 1
        else:
            # 2 campos diagonal / baixo
            if(tabuleiro_montado[ultima_linha+2][ultima_coluna-2] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id):
                vencedor = 1
            # 2 campos diagonal / cima
            elif(tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha-2][ultima_coluna+2] == ultimo_id):
                vencedor = 1
            # 1 diagonal / cima + 1 diagonal / baixo
            elif(tabuleiro_montado[ultima_linha-1][ultima_coluna+1] == ultimo_id) and (tabuleiro_montado[ultima_linha][ultima_coluna] == ultimo_id) and (tabuleiro_montado[ultima_linha+1][ultima_coluna-1] == ultimo_id):
                vencedor = 1

    # Verifica o empate
    for i in range(tabuleiro):
        for j in range(tabuleiro):
            if tabuleiro_montado[i][j] == 0:
                empate = 0

    if empate != 0:
        vencedor = 2
            
    
    # Informa o vencedor
    if vencedor == 1: # Houve vencedor
        # Pega o nome do vencedor
        for i in range(jogadores):
            if(lista_jogador[i][1] == ultimo_id):
                nome = str(lista_jogador[i][0])
        
        print("\nTABULEIRO FINAL: \n")
        exibe_tabuleiro()
        print("\n=================")
        print("\nVencedor: " + nome)
        print("\n=================\n")
        # Registra o resultado no arquivo
        arquivo = open(nome_arquivo+".txt", "a") # Abre o arquivo
        arquivo.writelines("Vencedor: " + nome) # Registra a informação
        arquivo.close() # Fecha o arquivo
        input("Pressione <ENTER> para finalizar")
        quit()
    elif vencedor == 2: # Empate
        print("\nTABULEIRO FINAL: \n")
        exibe_tabuleiro()
        print("\n=================")
        print("\nNão houve vencedor!")
        print("\n=================\n")
        # Registra o resultado no arquivo
        arquivo = open(nome_arquivo+".txt", "a") # Abre o arquivo
        arquivo.writelines("Não houve vencedor") # Registra a informação
        arquivo.close() # Fecha o arquivo
        input("Pressione <ENTER> para finalizar")
        quit()

# Validação de ID de jogador
def valida_id(verifica_id, tipo): # "tipo" é para poder validar ID repetido no cadastro, sendo 0 -> Cadastro; 1 -> Outros
    # Verifica se o ID é repetido
    if (int(tipo) == 0) and (len(lista_jogador)):
        for i in range(jogadores):
            if(lista_jogador[int(len(lista_jogador)-1)][1] == verifica_id):
                verifica_id = input("ID já utilizado!\nValor digitador: " + verifica_id + "\nPor favor, digite novamente o ID: ")

    # Verifica se o ID está no intervalo permitido
    while (int(verifica_id) > jogadores) or (int(verifica_id) <= 0):
        verifica_id = input("ID ultrapassa o limite permitido! Deve-se respeitar o intervalo ID[1," + str(jogadores) + "]\nValor digitador: " + verifica_id + "\nPor favor, digite novamente o ID: ")
        # Verifica se o ID é repetido
        if int(tipo) == 0:
            for i in range(jogadores):
                if(lista_jogador[i][1] == verifica_id):
                    verifica_id = input("ID já utilizado!\nValor digitador: " + verifica_id + "\nPor favor, digite novamente o ID: ")
    return verifica_id

# ====================
# MAIN
# ====================
# Recebe N = num_linhas e J = num_jogadores
qnt = input("Informe, respectivamente, o tamanho N do tabuleiro e a quantidade J de jogadores separados por espaço.\nObs.: N[3,10] e J[2,5]\nR: ").split(' ')
tabuleiro = int(qnt[0])
jogadores = int(qnt[1])

# Valida se o tamanho do tabuleiro é válido
while (tabuleiro < 3) or (tabuleiro > 10):
    tabuleiro = int(input("\nTamanho de tabuleiro inválido! Deve-se respeitar o intervalo N[3,10]\nValor digitado: " + str(tabuleiro) + "\nPor favor, digite novamente: "))

# Cria a matriz para o tabuleiro e monta o inicial
tabuleiro_montado = []
tabuleiro_inicial()
    
# Valida se a quantidade de jogadores é valida
while (jogadores < 2) or (jogadores > 5):
    jogadores = int(input("\nQuantidade de jogadores inválida! Deve-se respeitar o intervalo J[2,5]\nValor digitado: " + str(jogadores) + "\nPor favor, digite novamente: "))

# Atribui os valores de nome e ID aos jogadores
dados_jogador = []
lista_jogador = []

for i in range(jogadores):
    dados = input("Digite o nome e ID do " + str(i+1) + "o jogador separados por espaço.\nObs.: ID[1," + str(jogadores) + "]\nR: ").split(' ')
    dados_jogador.extend([dados[0], valida_id(dados[1], 0)]) # Valida se o ID está no intervalo permitido e atribui ao ID
    lista_jogador.extend([dados_jogador])
    dados_jogador = []

# Recebe o nome do arquivo a ser salvo
nome_arquivo = input("Digite o nome do arquivo de registro da partida: ")

# Inicia o jogo
while 1:
    # Exibe o tabuleiro
    print("\nTabuleiro:")
    exibe_tabuleiro()

    # Instruções ao jogador
    print("\nJOGADAS\nInstruções: Para jogar, digite, respectivamente, o ID do jogador, linha e coluna a serem preenchidas separadas por espaço.")

    # Recebe jogada
    jogada_efetuada = input("Digite sua jogada: ").split(' ')
    id_jogada = int(jogada_efetuada[0])
    linha_jogada = int(jogada_efetuada[1])
    coluna_jogada = int(jogada_efetuada[2])

    # Efetua a jogada
    jogada(id_jogada, linha_jogada, coluna_jogada)
