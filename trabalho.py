import numpy as np
def plotForcaY(forcas, grafico, posicao, compBarra, indice):
	if indice == 1:
		imagem = 30
	elif indice == 2:
		imagem = 55
	else:
		imagem = 80

	for i in range(0, len(forcas)):
		if type(forcas[i]) == str:
			posicaox = 0
			grafico[imagem*compBarra-17][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-16][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-15][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-14][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-13][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-12][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-11][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-10][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra-9][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-8][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-7][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-6][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-5][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]] = 255

			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]-2] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]+2] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra-2][25*compBarra + 50*posicao[i]] = 255
			
			ind = forcas[i].split()
			plotNumeros('v', posicao[i], compBarra, grafico, 0, posicaox, imagem)
			plotNumeros(int(ind[1]), posicao[i], compBarra, grafico, 1, posicaox, imagem)
			return grafico

		elif forcas[i] < 0:
			posicaox = 0
			grafico[imagem*compBarra-17][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-16][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-15][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-14][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-13][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-12][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-11][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-10][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra-9][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-8][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-7][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-6][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-5][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]] = 255

			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]-2] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra-4][25*compBarra + 50*posicao[i]+2] = 255
			grafico[imagem*compBarra-3][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra-2][25*compBarra + 50*posicao[i]] = 255
			forcas[i] *= -1
		else:
			posicaox = 20
			grafico[imagem*compBarra+17][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+16][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+15][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+14][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra+13][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+12][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+11][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+10][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra+9][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+8][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+7][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+6][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+5][25*compBarra + 50*posicao[i]] = 255	
			grafico[imagem*compBarra+4][25*compBarra + 50*posicao[i]] = 255

			grafico[imagem*compBarra+4][25*compBarra + 50*posicao[i]-2] = 255
			grafico[imagem*compBarra+4][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra+4][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra+3][25*compBarra + 50*posicao[i]-1] = 255
			grafico[imagem*compBarra+3][25*compBarra + 50*posicao[i]] = 255
			grafico[imagem*compBarra+4][25*compBarra + 50*posicao[i]+2] = 255
			grafico[imagem*compBarra+3][25*compBarra + 50*posicao[i]+1] = 255
			grafico[imagem*compBarra+2][25*compBarra + 50*posicao[i]] = 255

		forcaDecomposta = []
		while forcas[i] != 0:
			numero = forcas[i]%10
			forcas[i] = (forcas[i] - numero)// 10
			forcaDecomposta.insert(0, numero)
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[i], compBarra, grafico, j, posicaox, imagem)
			if j == len(forcaDecomposta)-1:
				plotNumeros('n', posicao[i], compBarra, grafico, j+1, posicaox, imagem)

	return grafico
def plotMomento(forcas, grafico, posicao, compBarra, indice):

	if indice == 1:
		imagem = 30
	elif indice == 2:
		imagem = 55
	else:
		imagem = 80

	for k in range(len(forcas)):
		if posicao[k] == 0:
			grafico[imagem*compBarra-3][25*compBarra-16] = 255
			grafico[imagem*compBarra-2][25*compBarra-16] = 255
			grafico[imagem*compBarra-1][25*compBarra-16] = 255
			grafico[imagem*compBarra][25*compBarra-16] = 255
			grafico[imagem*compBarra+1][25*compBarra-16] = 255
			grafico[imagem*compBarra+2][25*compBarra-16] = 255
			grafico[imagem*compBarra+3][25*compBarra-16] = 255

			grafico[imagem*compBarra-5][25*compBarra-14] = 255
			grafico[imagem*compBarra+5][25*compBarra-14] = 255
			grafico[imagem*compBarra-4][25*compBarra-15] = 255
			grafico[imagem*compBarra+4][25*compBarra-15] = 255

			grafico[imagem*compBarra-6][25*compBarra-13] = 255
			grafico[imagem*compBarra-6][25*compBarra-12] = 255
			grafico[imagem*compBarra-6][25*compBarra-11] = 255
			grafico[imagem*compBarra-6][25*compBarra-10] = 255
			grafico[imagem*compBarra-6][25*compBarra+1-10] = 255
			grafico[imagem*compBarra-6][25*compBarra+2-10] = 255
			grafico[imagem*compBarra-6][25*compBarra+3-10] = 255

			grafico[imagem*compBarra+6][25*compBarra-3-10] = 255
			grafico[imagem*compBarra+6][25*compBarra-2-10] = 255
			grafico[imagem*compBarra+6][25*compBarra-1-10] = 255
			grafico[imagem*compBarra+6][25*compBarra-10] = 255
			grafico[imagem*compBarra+6][25*compBarra+1-10] = 255
			grafico[imagem*compBarra+6][25*compBarra+2-10] = 255
			grafico[imagem*compBarra+6][25*compBarra+3-10] = 255


			if type(forcas[k]) == str:
				grafico[imagem*compBarra-8][25*compBarra+2-10] = 255
				grafico[imagem*compBarra-7][25*compBarra+3-10] = 255
				grafico[imagem*compBarra-6][25*compBarra+4-10] = 255
				grafico[imagem*compBarra-5][25*compBarra+3-10] = 255
				grafico[imagem*compBarra-4][25*compBarra+2-10] = 255
				
				ind = forcas[k].split()
				plotNumeros('m', posicao[k], compBarra, grafico, -6, 0, imagem)
				plotNumeros(int(ind[1]), posicao[k], compBarra, grafico, -4, 0, imagem)

				return grafico

			elif forcas[k] < 0:
				grafico[imagem*compBarra+4][25*compBarra+2-10] = 255
				grafico[imagem*compBarra+5][25*compBarra+3-10] = 255
				grafico[imagem*compBarra+6][25*compBarra+4-10] = 255
				grafico[imagem*compBarra+7][25*compBarra+3-10] = 255
				grafico[imagem*compBarra+8][25*compBarra+2-10] = 255
				forcas[k] *= -1

			else:
				grafico[imagem*compBarra-8][25*compBarra+2-10] = 255
				grafico[imagem*compBarra-7][25*compBarra+3-10] = 255
				grafico[imagem*compBarra-6][25*compBarra+4-10] = 255
				grafico[imagem*compBarra-5][25*compBarra+3-10] = 255
				grafico[imagem*compBarra-4][25*compBarra+2-10] = 255
				
		else:
			grafico[imagem*compBarra-3][75*compBarra+6+25] = 255
			grafico[imagem*compBarra-2][75*compBarra+6+25] = 255
			grafico[imagem*compBarra-1][75*compBarra+6+25] = 255
			grafico[imagem*compBarra][75*compBarra+6+25] = 255
			grafico[imagem*compBarra+1][75*compBarra+6+25] = 255
			grafico[imagem*compBarra+2][75*compBarra+6+25] = 255
			grafico[imagem*compBarra+3][75*compBarra+6+25] = 255

			grafico[imagem*compBarra-5][75*compBarra+4+25] = 255
			grafico[imagem*compBarra-4][75*compBarra+5+25] = 255
			grafico[imagem*compBarra+5][75*compBarra+4+25] = 255
			grafico[imagem*compBarra+4][75*compBarra+5+25] = 255

			grafico[imagem*compBarra-6][75*compBarra-3+25] = 255
			grafico[imagem*compBarra-6][75*compBarra-2+25] = 255
			grafico[imagem*compBarra-6][75*compBarra-1+25] = 255
			grafico[imagem*compBarra-6][75*compBarra+25] = 255
			grafico[imagem*compBarra-6][75*compBarra+1+25] = 255
			grafico[imagem*compBarra-6][75*compBarra+2+25] = 255
			grafico[imagem*compBarra-6][75*compBarra+3+25] = 255

			grafico[imagem*compBarra+6][75*compBarra-3+25] = 255
			grafico[imagem*compBarra+6][75*compBarra-2+25] = 255
			grafico[imagem*compBarra+6][75*compBarra-1+25] = 255
			grafico[imagem*compBarra+6][75*compBarra+25] = 255
			grafico[imagem*compBarra+6][75*compBarra+1+25] = 255
			grafico[imagem*compBarra+6][75*compBarra+2+25] = 255
			grafico[imagem*compBarra+6][75*compBarra+3+25] = 255

			if type(forcas[k]) == str:
				grafico[imagem*compBarra-8][75*compBarra-2+25] = 255
				grafico[imagem*compBarra-7][75*compBarra-3+25] = 255
				grafico[imagem*compBarra-6][75*compBarra-4+25] = 255
				grafico[imagem*compBarra-5][75*compBarra-3+25] = 255
				grafico[imagem*compBarra-4][75*compBarra-2+25] = 255

				ind = forcas[k].split()
				plotNumeros('m', posicao[k], compBarra, grafico, 4, 0, imagem)
				plotNumeros(int(ind[1]), posicao[k], compBarra, grafico, 4, 0, imagem)

				return grafico

			elif forcas[k] < 0:
				grafico[imagem*compBarra+4][75*compBarra-2+25] = 255
				grafico[imagem*compBarra+5][75*compBarra-3+25] = 255
				grafico[imagem*compBarra+6][75*compBarra-4+25] = 255
				grafico[imagem*compBarra+7][75*compBarra-3+25] = 255
				grafico[imagem*compBarra+8][75*compBarra-2+25] = 255
				forcas[k] *= -1

			else:
				grafico[imagem*compBarra-8][75*compBarra-2+25] = 255
				grafico[imagem*compBarra-7][75*compBarra-3+25] = 255
				grafico[imagem*compBarra-6][75*compBarra-4+25] = 255
				grafico[imagem*compBarra-5][75*compBarra-3+25] = 255
				grafico[imagem*compBarra-4][75*compBarra-2+25] = 255

		forcaDecomposta = []
		while forcas[k] != 0:
			numero = forcas[k]%10
			forcas[k] = (forcas[k] - numero)// 10
			forcaDecomposta.insert(0, numero)
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[k], compBarra, grafico, j+1, 0, imagem)
			if j == len(forcaDecomposta)-1:
				plotNumeros('n', posicao[k], compBarra, grafico, j+2, 0, imagem)
				plotNumeros('m', posicao[k], compBarra, grafico, j+2, 0, imagem)
	return grafico

	
def plotEngaste(grafico, posicao, compBarra, indice):

	if indice == 1:
		imagem = 30

	if posicao == 0:
		grafico[imagem*compBarra-1][25*compBarra] = 255
		grafico[imagem*compBarra-2][25*compBarra] = 255
		grafico[imagem*compBarra-3][25*compBarra] = 255
		grafico[imagem*compBarra-4][25*compBarra] = 255
		grafico[imagem*compBarra-5][25*compBarra] = 255
		grafico[imagem*compBarra][25*compBarra] = 255
		grafico[imagem*compBarra+1][25*compBarra] = 255
		grafico[imagem*compBarra+2][25*compBarra] = 255
		grafico[imagem*compBarra+3][25*compBarra] = 255
		grafico[imagem*compBarra+4][25*compBarra] = 255
		grafico[imagem*compBarra+5][25*compBarra] = 255

		grafico[imagem*compBarra-3][25*compBarra-3] = 255
		grafico[imagem*compBarra-4][25*compBarra-2] = 255
		grafico[imagem*compBarra-5][25*compBarra-1] = 255

		grafico[imagem*compBarra][25*compBarra-1] = 255
		grafico[imagem*compBarra+1][25*compBarra-2] = 255
		grafico[imagem*compBarra+2][25*compBarra-3] = 255

		grafico[imagem*compBarra+5][25*compBarra-1] = 255
		grafico[imagem*compBarra+6][25*compBarra-2] = 255
		grafico[imagem*compBarra+7][25*compBarra-3] = 255
	else:
		grafico[imagem*compBarra-1][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra-2][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra-3][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra-4][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra-5][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra+1][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra+2][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra+3][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra+4][25*compBarra+ 50*posicao] = 255
		grafico[imagem*compBarra+5][25*compBarra+ 50*posicao] = 255

		grafico[imagem*compBarra-3][25*compBarra+3+ 50*posicao] = 255
		grafico[imagem*compBarra-4][25*compBarra+2+ 50*posicao] = 255
		grafico[imagem*compBarra-5][25*compBarra+1+ 50*posicao] = 255

		grafico[imagem*compBarra][25*compBarra+1+ 50*posicao] = 255
		grafico[imagem*compBarra+1][25*compBarra+2+ 50*posicao] = 255
		grafico[imagem*compBarra+2][25*compBarra+3+ 50*posicao] = 255

		grafico[imagem*compBarra+5][25*compBarra+1+ 50*posicao] = 255
		grafico[imagem*compBarra+6][25*compBarra+2+ 50*posicao] = 255
		grafico[imagem*compBarra+7][25*compBarra+3+ 50*posicao] = 255

	

	return grafico
		
def plotApoioSimples(grafico, posicao, compBarra, indice):

	if indice == 1:
		imagem = 30

	grafico[imagem*compBarra+1][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+1][25*compBarra + 50*posicao-1] = 255

	grafico[imagem*compBarra+2][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao-2] = 255

	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-3] = 255

	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-3] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+4] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-4] = 255

	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-3] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+4] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-4] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+5] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-5] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+6] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-6] = 255

	grafico[imagem*compBarra+1][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao] = 255
	
	return grafico
def plotApoioDuplo(grafico, posicao, compBarra, indice):
	if indice == 1:
		imagem = 30

	grafico[imagem*compBarra+1][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+1][25*compBarra + 50*posicao-1] = 255

	grafico[imagem*compBarra+2][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao-2] = 255

	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao-3] = 255

	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-3] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao+4] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao-4] = 255

	grafico[imagem*compBarra+5][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao-3] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao+4] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao-4] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao+5] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao-5] = 255

	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+1] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-1] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+2] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-2] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+3] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-3] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+4] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-4] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+5] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-5] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao+6] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao-6] = 255

	grafico[imagem*compBarra+1][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+2][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+3][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+4][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+5][25*compBarra + 50*posicao] = 255
	grafico[imagem*compBarra+6][25*compBarra + 50*posicao] = 255

	return grafico

def plotForcaX(forcas, grafico, posicao, compBarra, indice):
	if indice == 1:
		imagem = 30
	elif indice == 2:
		imagem = 55
	else:
		imagem = 80
	for i in range(0, len(forcas)):
		if posicao[i] == 0:
			grafico[imagem*compBarra][25*compBarra-1] = 255
			grafico[imagem*compBarra][25*compBarra-2] = 255	
			grafico[imagem*compBarra][25*compBarra-3] = 255
			grafico[imagem*compBarra][25*compBarra-4] = 255
			grafico[imagem*compBarra][25*compBarra-5] = 255	
			grafico[imagem*compBarra][25*compBarra-6] = 255
			grafico[imagem*compBarra][25*compBarra-7] = 255

			if type(forcas[i]) == str:

				grafico[imagem*compBarra-1][25*compBarra-2] = 255
				grafico[imagem*compBarra+1][25*compBarra-2] = 255
				grafico[imagem*compBarra-2][25*compBarra-3] = 255
				grafico[imagem*compBarra+2][25*compBarra-3] = 255

				ind = forcas[i].split()
				plotNumeros('h', posicao[i], compBarra, grafico, -1, 15, imagem)
				plotNumeros(int(ind[1]), posicao[i], compBarra, grafico, 0, 15, imagem)

				return grafico

			elif forcas[i] < 0:
				grafico[imagem*compBarra-1][25*compBarra] = 255
				grafico[imagem*compBarra-2][25*compBarra+1] = 255
				grafico[imagem*compBarra+1][25*compBarra] = 255
				grafico[imagem*compBarra+2][25*compBarra+1] = 255
				grafico[imagem*compBarra][25*compBarra-1] = 255
				forcas[i] *= -1
			else: 
				grafico[imagem*compBarra-1][25*compBarra-2] = 255
				grafico[imagem*compBarra+1][25*compBarra-2] = 255
				grafico[imagem*compBarra-2][25*compBarra-3] = 255
				grafico[imagem*compBarra+2][25*compBarra-3] = 255
		else:
			grafico[imagem*compBarra][75*compBarra] = 255
			grafico[imagem*compBarra][75*compBarra+1] = 255	
			grafico[imagem*compBarra][75*compBarra+2] = 255
			grafico[imagem*compBarra][75*compBarra+3] = 255
			grafico[imagem*compBarra][75*compBarra+4] = 255	
			grafico[imagem*compBarra][75*compBarra+5] = 255
			grafico[imagem*compBarra][75*compBarra+6] = 255

			if type(forcas[i]) == str:
				grafico[imagem*compBarra-1][75*compBarra+6] = 255
				grafico[imagem*compBarra-2][75*compBarra+5] = 255
				grafico[imagem*compBarra+1][75*compBarra+6] = 255
				grafico[imagem*compBarra+2][75*compBarra+5] = 255
				grafico[imagem*compBarra][75*compBarra+7] = 255

				ind = forcas[i].split()
				plotNumeros('h', posicao[i], compBarra, grafico, -1, 15, imagem)
				plotNumeros(int(ind[1]), posicao[i], compBarra, grafico, 0, 15, imagem)

				return grafico
				
			elif forcas[i] < 0:
				grafico[imagem*compBarra-1][75*compBarra] = 255
				grafico[imagem*compBarra-2][75*compBarra+1] = 255
				grafico[imagem*compBarra+1][75*compBarra] = 255
				grafico[imagem*compBarra+2][75*compBarra+1] = 255
				grafico[imagem*compBarra][75*compBarra] = 255
				forcas[i] *= -1

			else: 
				grafico[imagem*compBarra-1][75*compBarra+6] = 255
				grafico[imagem*compBarra-2][75*compBarra+5] = 255
				grafico[imagem*compBarra+1][75*compBarra+6] = 255
				grafico[imagem*compBarra+2][75*compBarra+5] = 255
				grafico[imagem*compBarra][75*compBarra+7] = 255

		forcaDecomposta = []
		while forcas[i] != 0:
			numero = forcas[i]%10
			forcas[i] = (forcas[i] - numero)// 10
			forcaDecomposta.insert(0, int(numero))
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[i], compBarra, grafico, j-1, 0, imagem)
			if j == len(forcaDecomposta)-1:
				plotNumeros('n', posicao[i], compBarra, grafico, j, 0, imagem)

	return grafico

def plotNumeros(num, posicao, compBarra, grafico, qtd, posicaox, imagem):
	if num == 0:
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	if num == 1:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255

		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	if num == 2:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	elif num == 3:
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 5050*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	elif num == 4:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	elif num == 5:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
	elif num == 6:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
	elif num == 7:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

	elif num == 8:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		
	elif num == 9:
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	elif num == 'n':
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255

		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+6+7*qtd+3] = 255
	elif num == 'm':
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+10+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+11+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+13+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+14+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255
	elif num == 'h':
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		
	elif num == 'v':
		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[imagem*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[imagem*compBarra-7+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255

		grafico[imagem*compBarra-6+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[imagem*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255




	return grafico

def plot(compBarra, forcas, posicao, solucao):
	n = 100*compBarra

	plotGrafico = open('diagramas.pgm', 'w')
	plotGrafico.write('\n P2 \n')
	plotGrafico.write(str(n)+ ' '+str(n))
	plotGrafico.write('\n 255 \n')
	grafico = []

	for i in range (0, 100*compBarra):
		linha = []
		for j in range(100*compBarra):
			linha.append(0)
		grafico.append(linha)

	for x in range(25*compBarra, 75*compBarra):
		grafico[30*compBarra-1][x] = 255
		grafico[30*compBarra][x] = 255
		grafico[30*compBarra+1][x] = 255

		grafico[55*compBarra-1][x] = 255
		grafico[55*compBarra][x] = 255
		grafico[55*compBarra+1][x] = 255

		grafico[80*compBarra-1][x] = 255
		grafico[80*compBarra][x] = 255
		grafico[80*compBarra+1][x] = 255

	if (len(forcas[0]) == 1 and forcas[0][0] != 0) or len(forcas[0]) != 1:
		grafico = plotForcaX(forcas[0], grafico, posicao[0], compBarra, 1)

	if (len(forcas[1]) == 1 and forcas[1][0] != 0) or len(forcas[1]) != 1:
		grafico = plotForcaY(forcas[1], grafico, posicao[1], compBarra, 1)

	if (len(forcas[2]) == 1 and forcas[2][0] != 0) or len(forcas[2]) != 1:
		grafico = plotMomento(forcas[2], grafico, posicao[2], compBarra, 1)

	if len(forcas[3][0]) != 0:
		for i in range (len(forcas[3][0])):
			grafico = plotApoioSimples(grafico, forcas[3][0][i], compBarra, 1)

	if len(forcas[3][1]) != 0:
		for i in range (len(forcas[3][1])):
			grafico = plotApoioDuplo(grafico, forcas[3][1][i], compBarra, 1)

	if len(forcas[3][2]) != 0:
		for i in range (len(forcas[3][2])):
			grafico = plotEngaste(grafico, forcas[3][2][i], compBarra, 1)
			
	########################################################################

	if (len(solucao[0]) == 1 and solucao[0][0] != 0) or len(solucao[0]) != 1:
		grafico = plotForcaX(solucao[0], grafico, posicao[0], compBarra, 3)

	if (len(solucao[1]) == 1 and solucao[1][0] != 0) or len(solucao[1]) != 1:
		grafico = plotForcaY(solucao[1], grafico, posicao[1], compBarra, 3)

	if (len(solucao[2]) == 1 and solucao[2][0] != 0) or len(solucao[2]) != 1:
		grafico = plotMomento(solucao[2], grafico, posicao[2], compBarra, 3)

	########################################################################
	

	if (len(forcas[0]) == 1 and forcas[0][0] != 0) or len(forcas[0]) != 1:
		grafico = plotForcaX(forcas[0], grafico, posicao[0], compBarra, 2)

	if (len(forcas[1]) == 1 and forcas[1][0] != 0) or len(forcas[1]) != 1:
		grafico = plotForcaY(forcas[1], grafico, posicao[1], compBarra, 2)

	if (len(forcas[2]) == 1 and forcas[2][0] != 0) or len(forcas[2]) != 1:
		grafico = plotMomento(forcas[2], grafico, posicao[2], compBarra, 2)

	if len(forcas[3][0]) != 0:
		for i in range (len(forcas[3][0])):
			grafico = plotForcaY(["v "+str(i+1)], grafico, forcas[3][0], compBarra, 2)	

	if len(forcas[3][1]) != 0:
		for i in range (len(forcas[3][1])):
			grafico = plotForcaY(["v "+str(i+1)], grafico, forcas[3][1], compBarra, 2)	
			grafico = plotForcaX(["h "+str(i+1)], grafico, forcas[3][1], compBarra, 2)		

	if len(forcas[3][2]) != 0:
		for i in range (len(forcas[3][2])):
			grafico = plotForcaX(["h "+str(i+1)], grafico, forcas[3][2], compBarra, 2)
			grafico = plotForcaY(["v "+str(i+1)], grafico, forcas[3][2], compBarra, 2)
			grafico = plotMomento(["m "+str(i+1)], grafico, forcas[3][2], compBarra, 2)


	for i in range (0, 100*compBarra):
		for j in range(0, 100*compBarra):
			plotGrafico.write(str(grafico[i][j])+' ')
		plotGrafico.write('\n')
	plotGrafico.close()
