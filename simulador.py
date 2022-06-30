import numpy as np
from trabalho import plot

def simulador():
    modForcas = []
    modForcasX, modForcasY = [], []

    posForcas = []
    posForcasX, posForcasY = [], []

    apoios = []
    engastes, simples, duplos = [], [], []

    momentos = []
    reacoesEngastes, reacoesSimples, reacoesDuplos = [], [], []

    zero = [0.0]

    # Configuração da barra
    print("Bem-vindo ao simulador de esforços!\nInsira o comprimento da sua barra (metros):")
    comprimento = float(input())

    while(comprimento <= 0):
        print("O comprimento da barra deve ser maior que 0")
        comprimento = float(input())

    print("\nComprimento de " + str(comprimento) + " metros configurado com sucesso!\n")
    print("-------------------------------------------------\n")

    # Configuração dos três tipos de apoio
    print("Configuração dos apoios\nDeseja adicionar engastamentos?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira posição horizontal do engaste: ")
        posicaoAtual = float(input()) 

        if posicaoAtual != 0 and posicaoAtual != comprimento:
            print("Posição inválida. Um engaste deve ser posicionado no início ou no final da barra.")

        elif posicaoAtual < 0:
            print("Posição inválida. Insira uma posição maior ou igual a zero.")

        else:
            engastes.append(posicaoAtual)

        print("Deseja inserir mais engastes? (sim/nao)")
        continua = input()

    if len(engastes) != 0:
        print("\nEngastes configurados com sucesso nas posições: " + str(engastes) + " (metros).")
    else: 
        print("\n Não há engastes no sistema.")
    print("-------------------------------------------------\n")
    
    print("Deseja adicionar apoios simples?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira posição horizontal do apoio simples: ")
        posicaoAtual = float(input()) 

        if posicaoAtual > comprimento:
            print("Posição inválida. Insira uma posição menor ou igual ao comprimento da barra.")

        elif posicaoAtual < 0:
            print("Posição inválida. Insira uma posição maior ou igual a zero.")

        else:
            simples.append(posicaoAtual)

        print("Deseja inserir mais apoios simples? (sim/nao)")
        continua = input()

    if len(simples) != 0:
        print("\nApoios simples configurados com sucesso nas posições: " + str(simples) + " (metros).")
    else: 
        print("\n Não há apoios simples no sistema.")
    print("-------------------------------------------------\n")

    print("Deseja adicionar apoios duplos?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira posição horizontal do apoio duplo: ")
        posicaoAtual = float(input()) 

        if posicaoAtual > comprimento:
            print("Posição inválida. Insira uma posição menor ou igual ao comprimento da barra.")

        elif posicaoAtual < 0:
            print("Posição inválida. Insira uma posição maior ou igual a zero.")

        else:
            duplos.append(posicaoAtual)

        print("Deseja inserir mais apoios duplos? (sim/nao)")
        continua = input()

    if len(duplos) != 0:
        print("\nApoios duplos configurados com sucesso nas posições: " + str(duplos) + " (metros).")
    else: 
        print("\n Não há apoios duplos no sistema.")
    print("-------------------------------------------------\n")

    if(len(simples) != 0):
        apoios.append(simples)
    else:
        apoios.append(zero)

    if(len(duplos) != 0):
        apoios.append(duplos)
    else:
        apoios.append(zero)

    if(len(engastes) != 0):
        apoios.append(engastes)
    else:
        apoios.append(zero)
    

    # Configuração dos esforços
    print("Configuração dos esforços\nDeseja aplicar forças na direção horizontal (eixo x)?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira o módulo da força horizontal a ser adicionada: ")
        moduloAtual = float(input())

        print("Insira a posição do ponto de aplicação da força a ser adicionada: ")
        posicaoAtual = float(input())

        if posicaoAtual != 0 and posicaoAtual != comprimento:
            print("Posição inválida. Uma força horizontal deve ser aplicada no começo ou no final da barra")
            print("A força não foi adicionada.\n")
        else:
            posForcasX.append(posicaoAtual)
            modForcasX.append(moduloAtual)

        print("Deseja aplicar mais forças na direção horizontal? (sim/nao)")
        continua = input()

    if len(modForcasX) != 0:
        print("\nForças horizontais de módulo" + str(modForcasX) + " (Newtons) aplicadas com sucesso nas posições: " 
        + str(posForcasX) + " (metros) respectivamente.")
    else: 
        print("\n Não há forças horizontais aplicadas no sistema.")
    print("-------------------------------------------------\n")

    print("Deseja aplicar forças na direção vertical (eixo y)?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira o módulo da força vertical a ser adicionada: ")
        moduloAtual = float(input())

        print("Insira a posição horizontal do ponto de aplicação da força a ser adicionada: ")
        posicaoAtual = float(input())

        if posicaoAtual > comprimento:
            print("Posição inválida. Insira uma posição menor ou igual ao comprimento da barra.")
            print("A força não foi adicionada.\n")

        elif posicaoAtual < 0:
            print("Posição inválida. Insira uma posição maior ou igual a zero.")
            print("A força não foi adicionada.\n")

        else:
            posForcasY.append(posicaoAtual)
            modForcasY.append(moduloAtual)

        print("Deseja aplicar mais forças na direção vertical? (sim/nao)")
        continua = input()

    if len(modForcasY) != 0:
        print("\nForças verticais de módulo" + str(modForcasY) + " (Newtons) aplicadas com sucesso nas posições: " 
        + str(posForcasY) + " (metros) respectivamente.")
    else: 
        print("\n Não há forças verticais aplicadas no sistema.")
    print("-------------------------------------------------\n")

    modForcas.append(modForcasX)
    modForcas.append(modForcasY)

    posForcas.append(posForcasX)
    posForcas.append(posForcasY)

    # Resultante das forças
    resForcasY = sum(modForcasY)
    resForcasX = sum(modForcasX)

    
    # 1 apoio simples e 1 apoio duplo
    if (len(engastes) == 0 and  len(simples) == 1 and len(duplos) == 1):
        if (len(modForcasX) != 0):
            reacoesDuplos.append(-sum(modForcasX))
        else:
            reacoesDuplos.append(0.0)
        for i in range(len(modForcasY)):
            momentos.append(modForcasY[i] * (posForcasY[i] - simples[0]))
        reacoesDuplos.append(- sum(momentos) / (duplos[0] - simples[0]))
        reacoesSimples.append(- sum(modForcasY) - reacoesDuplos[1])
        print("reacoes apoio duplo: " + str(reacoesDuplos) + "\n" + "reacoes apoio simples: " + str(reacoesSimples))
    
    # 1 engaste
    if (len(engastes) == 1 and  len(simples) == 0 and len(duplos) == 0):
        for i in range(len(modForcasY)):
            momentos.append(modForcasY[i] * (posForcasY[i] - engastes[0]))
        if (len(modForcasX) != 0):
            reacoesEngastes.append(- sum(modForcasX))
        else:
            reacoesEngastes.append(0.0)
        reacoesEngastes.append(- sum(modForcasY))
        reacoesEngastes.append(- sum(momentos))
        print("reacoes engaste: " + str(reacoesEngastes))
    
    matrizForcas = matrizForcasPlot(modForcasX, modForcasY, momentos, apoios)
    matrizPosicoes = matrizPosPlot(comprimento, posForcasX, posForcasY, momentos, apoios)

    plot(comprimento, matrizForcas, matrizPosicoes)

def matrizForcasPlot(forcasX, forcasY, momentos, apoios):

    matrizForcas = []
    if(len(forcasX) != 0):
        fx = np.zeros((1, len(forcasX)))
        for i in range(len(forcasX)):
            fx[0][i] = forcasX[i]
    else:
        fx = np.zeros((1,1))

    if(len(forcasY) != 0):
        fy = np.zeros((1, len(forcasY)))
        for i in range(len(forcasY)):
            fy[0][i] = forcasY[i]
    else:
        fy = np.zeros((1, 1))

    mom = np.zeros((1,1))
    mom[0][0] = sum(momentos)

    if(len(apoios) != 0):
        apoio = np.zeros((1, len(apoios)))
        for i in range(len(apoios)):
            apoio[0][i] = apoios[i][0]
    else:
        apoio = np.zeros((1,1))
        
    matrizForcas.append(fx)
    matrizForcas.append(fy)
    matrizForcas.append(mom)
    matrizForcas.append(apoio)

    return matrizForcas


def matrizPosPlot(barra, posicoesX, posicoesY, momentos, apoios):

    matrizPosicoes = []
    if(len(posicoesX) != 0):
        px = np.zeros((1, len(posicoesX)))
        for i in range(len(posicoesX)):
            px[0][i] = posicoesX[i]
    else:
        px = np.zeros((1,1))

    if(len(posicoesY) != 0):
        py = np.zeros((1, len(posicoesY)))
        for i in range(len(posicoesY)):
            py[0][i] = posicoesY[i]
    else:
        py = np.zeros((1, 1))

    mom = np.zeros((1,1))
    mom[0][0] = barra

    if(len(apoios) != 0):
        apoio = np.zeros((1, len(apoios)))
        for i in range(len(apoios)):
            apoio[0][i] = apoios[i][0]
    else:
        apoio = np.zeros((1,1))
        
    matrizPosicoes.append(px)
    matrizPosicoes.append(py)
    matrizPosicoes.append(mom)
    matrizPosicoes.append(apoio)

    return matrizPosicoes

simulador()





