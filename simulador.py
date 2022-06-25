def simulador():
    modForcas = []
    modForcasX, modForcasY = [], []

    posForcas = []
    posForcasX, posForcasY = [], []

    apoios = []
    engastes, simples, duplos = [], [], []

    # Configuração da barra
    print("Bem-vindo ao simulador de esforços!\nInsira o comprimento da sua barra (metros):")
    comprimento = int(input())

    while(comprimento <= 0):
        print("O comprimento da barra deve ser maior que 0")
        comprimento = int(input())

    print("\nComprimento de " + str(comprimento) + " metros configurado com sucesso!\n")
    print("-------------------------------------------------\n")

    # Configuração dos três tipos de apoio
    print("Configuração dos apoios\nDeseja adicionar engastamentos?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira posição horizontal do engaste: ")
        posicaoAtual = int(input()) 

        if posicaoAtual < comprimento or posicaoAtual > 0:
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
        posicaoAtual = int(input()) 

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
        posicaoAtual = int(input()) 

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

    apoios.append(engastes)
    apoios.append(simples)
    apoios.append(duplos)

    # Configuração dos esforços
    print("Configuração dos esforços\nDeseja aplicar forças na direção horizontal (eixo x)?(sim/nao)")
    continua = input()

    while continua == 'sim':
        print("Insira o módulo da força horizontal a ser adicionada: ")
        modForcasX.append(int(input()))

        print("Insira a posição do ponto de aplicação da força a ser adicionada: ")
        posicaoAtual = int(input())

        if posicaoAtual > 0 or posicaoAtual < comprimento:
            print("Posição inválida. Uma força horizontal deve ser aplicada no começo ou no final da barra")
        else:
            posForcasX.append(posicaoAtual)

        print("Deseja aplicar mais forças na drieção vertical? (sim/nao)")
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
        modForcasY.append(int(input()))

        print("Insira a posição horizontal do ponto de aplicação da força a ser adicionada: ")
        posicaoAtual = int(input())

        if posicaoAtual > comprimento:
            print("Posição inválida. Insira uma posição menor ou igual ao comprimento da barra.")

        elif posicaoAtual < 0:
            print("Posição inválida. Insira uma posição maior ou igual a zero.")

        else:
            posForcasY.append(posicaoAtual)

        print("Deseja aplicar mais forças na drieção vertical? (sim/nao)")
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

simulador()