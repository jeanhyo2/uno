import random

# Definição das cartas de cada cor
amarelo = [0,1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2',1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2','coringa','coringa+4']
azul = [0,1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2',1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2','coringa','coringa+4']
verde = [0,1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2',1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2','coringa','coringa+4']
vermelho = [0,1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2',1,2,3,4,5,6,7,8,9,'negar','voltar','mais 2','coringa','coringa+4']

mao = []

# Função de compra
def comprar(amarelo, azul, verde, vermelho):
    randcor = random.randint(1, 4)
    if randcor == 1:
        cor = 'amarelo'
        randcor = amarelo
    elif randcor == 2:
        cor = 'azul'
        randcor = azul
    elif randcor == 3:
        cor = 'verde'
        randcor = verde
    else:
        cor = 'vermelho'
        randcor = vermelho

    randnum = random.randint(0, len(randcor) - 1)
    carta = randcor.pop(randnum)
    return (cor, carta)

# Mão inicial
for i in range(7):
    mao.append(comprar(amarelo, azul, verde, vermelho))

print("Mão inicial:", mao)

# Início do jogo
while True:
    topo = input("Qual a carta do topo? (no formato 'cor numero', caso seja uma carta de ação deve ser no formato 'cor ação')  ")
    partes = topo.split()
    
    # Verifica se a entrada tem exatamente duas partes
    if len(partes) != 2:
        print("Formato de entrada inválido. Certifique-se de usar o formato 'cor numero'.")
        continue
    
    cortopo = partes[0]
    numtopo = partes[1]
    
    # Verifica se a cor está na lista de cores permitidas
    if cortopo not in ['amarelo', 'azul', 'verde', 'vermelho']:
        print("Cor incorreta. As cores permitidas são: amarelo, azul, verde, vermelho.")
        continue
    
    # Remove a carta do topo das listas de cartas disponíveis para compra
    if cortopo == 'amarelo' and numtopo in amarelo:
        amarelo.remove(numtopo)
    elif cortopo == 'azul' and numtopo in azul:
        azul.remove(numtopo)
    elif cortopo == 'verde' and numtopo in verde:
        verde.remove(numtopo)
    elif cortopo == 'vermelho' and numtopo in vermelho:
        vermelho.remove(numtopo)

    print("Carta do topo:", cortopo, numtopo)

#cartas especiais
        # Se a carta do topo for "mais 2"
    if numtopo == 'mais 2':
        for _ in range(2):
            mao.append(comprar(amarelo, azul, verde, vermelho))
        mensagensdois = [
            "Carta 'mais 2' comprei 2 cartas e criei ódio por voce!",
            "Carta 'mais 2' eu compro 2 cartas e reduzo sua espectativa de vida em 2 anos!",
            "Carta 'mais 2'??? é assim que vc me trata??? ",
            "Carta 'mais 2'? tem certeza? olha que vou contar pra todo mundo que você esta roubando heim!"
        ]
        print(random.choice(mensagensdois))
        continue

        # Se a carta do topo for "coringa+4
    if numtopo == 'coringa+4':
        for _ in range(4):
            mao.append(comprar(amarelo, azul, verde, vermelho))
        mensagensquatro = [
            "Carta 'coringa+4' assim acaba com a amizade!",
            "Carta 'coringa+4' VAI PRA PQP!",
            "Carta 'coringa+4??? é assim que vc me trata??? ",
            "Carta 'coringa+4'? NAO QUERO MAIS JOGAR!!!!"
        ]
        mensagem_escolhida = random.choice(mensagensquatro)
        print(mensagem_escolhida)
        if mensagem_escolhida == mensagensquatro[3]:  # Verifica se vai dar rage e parar de jogar
            break  # Termina o jogo
        continue

        # Se a carta do topo for "negar", apenas pergunta de novo a carta do topo
    if numtopo == 'negar':
        print("Carta 'negar', passando a vez e a mão na perna da sua namorada...")
        continue


    # Tenta jogar uma carta da mão
    carta_jogada = None
    for carta in mao:
        cor, numero = carta
        if cor == cortopo or str(numero) == numtopo:
            carta_jogada = carta
            break

    if carta_jogada:
        mao.remove(carta_jogada)
        print("Carta jogada:", carta_jogada)
    else:
        nova_carta = comprar(amarelo, azul, verde, vermelho)
        mao.append(nova_carta)
        print("Não tinha carta correspondente na mão, comprou nova carta:", nova_carta)

    print("Mão atual:", mao)

    #verifica se tem UNO ou se ganhou
    if len(mao) == 1:
        print("UNO!")
    elif len(mao) == 0:
        print("GANHEI!")
        break  # Termina o jogo
