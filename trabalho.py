import os
import numpy as np
def plotForcaY(forcas, grafico, posicao, compBarra):
	for i in range(0, len(forcas)):
		if forcas[i] < 0:
			posicaox = 0
			grafico[50*compBarra-17][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-16][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-15][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-14][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-13][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-12][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-11][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-10][25*compBarra + 50*posicao[i]] = 255	
			grafico[50*compBarra-9][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-8][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-7][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-6][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-5][25*compBarra + 50*posicao[i]] = 255	
			grafico[50*compBarra-4][25*compBarra + 50*posicao[i]] = 255

			grafico[50*compBarra-4][25*compBarra + 50*posicao[i]-2] = 255
			grafico[50*compBarra-4][25*compBarra + 50*posicao[i]-1] = 255
			grafico[50*compBarra-4][25*compBarra + 50*posicao[i]+1] = 255
			grafico[50*compBarra-3][25*compBarra + 50*posicao[i]-1] = 255
			grafico[50*compBarra-3][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra-4][25*compBarra + 50*posicao[i]+2] = 255
			grafico[50*compBarra-3][25*compBarra + 50*posicao[i]+1] = 255
			grafico[50*compBarra-2][25*compBarra + 50*posicao[i]] = 255
			forcas[i] *= -1
		else:
			posicaox = 20
			grafico[50*compBarra+17][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+16][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+15][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+14][25*compBarra + 50*posicao[i]] = 255	
			grafico[50*compBarra+13][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+12][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+11][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+10][25*compBarra + 50*posicao[i]] = 255	
			grafico[50*compBarra+9][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+8][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+7][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+6][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+5][25*compBarra + 50*posicao[i]] = 255	
			grafico[50*compBarra+4][25*compBarra + 50*posicao[i]] = 255

			grafico[50*compBarra+4][25*compBarra + 50*posicao[i]-2] = 255
			grafico[50*compBarra+4][25*compBarra + 50*posicao[i]-1] = 255
			grafico[50*compBarra+4][25*compBarra + 50*posicao[i]+1] = 255
			grafico[50*compBarra+3][25*compBarra + 50*posicao[i]-1] = 255
			grafico[50*compBarra+3][25*compBarra + 50*posicao[i]] = 255
			grafico[50*compBarra+4][25*compBarra + 50*posicao[i]+2] = 255
			grafico[50*compBarra+3][25*compBarra + 50*posicao[i]+1] = 255
			grafico[50*compBarra+2][25*compBarra + 50*posicao[i]] = 255

		forcaDecomposta = []
		while forcas[i] != 0:
			numero = forcas[i]%10
			forcas[i] = (forcas[i] - numero)// 10
			forcaDecomposta.insert(0, numero)
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[i], compBarra, grafico, j, posicaox)
		if j == len(forcaDecomposta)-1:
			plotNumeros('n', posicao[i], compBarra, grafico, j+1, posicaox)

	return grafico
def plotMomento(forcas, grafico, posicao, compBarra):
	for k in range(len(forcas)):
		if posicao[k] == 0:
			grafico[50*compBarra-3][25*compBarra-6] = 255
			grafico[50*compBarra-2][25*compBarra-6] = 255
			grafico[50*compBarra-1][25*compBarra-6] = 255
			grafico[50*compBarra][25*compBarra-6] = 255
			grafico[50*compBarra+1][25*compBarra-6] = 255
			grafico[50*compBarra+2][25*compBarra-6] = 255
			grafico[50*compBarra+3][25*compBarra-6] = 255

			grafico[50*compBarra-5][25*compBarra-4] = 255
			grafico[50*compBarra+5][25*compBarra-4] = 255
			grafico[50*compBarra-4][25*compBarra-5] = 255
			grafico[50*compBarra+4][25*compBarra-5] = 255

			grafico[50*compBarra-6][25*compBarra-3] = 255
			grafico[50*compBarra-6][25*compBarra-2] = 255
			grafico[50*compBarra-6][25*compBarra-1] = 255
			grafico[50*compBarra-6][25*compBarra] = 255
			grafico[50*compBarra-6][25*compBarra+1] = 255
			grafico[50*compBarra-6][25*compBarra+2] = 255
			grafico[50*compBarra-6][25*compBarra+3] = 255

			grafico[50*compBarra+6][25*compBarra-3] = 255
			grafico[50*compBarra+6][25*compBarra-2] = 255
			grafico[50*compBarra+6][25*compBarra-1] = 255
			grafico[50*compBarra+6][25*compBarra] = 255
			grafico[50*compBarra+6][25*compBarra+1] = 255
			grafico[50*compBarra+6][25*compBarra+2] = 255
			grafico[50*compBarra+6][25*compBarra+3] = 255

			if forcas[k] < 0:
				grafico[50*compBarra+4][25*compBarra+2] = 255
				grafico[50*compBarra+5][25*compBarra+3] = 255
				grafico[50*compBarra+6][25*compBarra+4] = 255
				grafico[50*compBarra+7][25*compBarra+3] = 255
				grafico[50*compBarra+8][25*compBarra+2] = 255
				forcas[k] *= -1
			else:
				grafico[50*compBarra-8][25*compBarra+2] = 255
				grafico[50*compBarra-7][25*compBarra+3] = 255
				grafico[50*compBarra-6][25*compBarra+4] = 255
				grafico[50*compBarra-5][25*compBarra+3] = 255
				grafico[50*compBarra-4][25*compBarra+2] = 255
				
		else:
			grafico[50*compBarra-3][75*compBarra+6] = 255
			grafico[50*compBarra-2][75*compBarra+6] = 255
			grafico[50*compBarra-1][75*compBarra+6] = 255
			grafico[50*compBarra][75*compBarra+6] = 255
			grafico[50*compBarra+1][75*compBarra+6] = 255
			grafico[50*compBarra+2][75*compBarra+6] = 255
			grafico[50*compBarra+3][75*compBarra+6] = 255

			grafico[50*compBarra-5][75*compBarra+4] = 255
			grafico[50*compBarra-4][75*compBarra+5] = 255
			grafico[50*compBarra+5][75*compBarra+4] = 255
			grafico[50*compBarra+4][75*compBarra+5] = 255

			grafico[50*compBarra-6][75*compBarra-3] = 255
			grafico[50*compBarra-6][75*compBarra-2] = 255
			grafico[50*compBarra-6][75*compBarra-1] = 255
			grafico[50*compBarra-6][75*compBarra] = 255
			grafico[50*compBarra-6][75*compBarra+1] = 255
			grafico[50*compBarra-6][75*compBarra+2] = 255
			grafico[50*compBarra-6][75*compBarra+3] = 255

			grafico[50*compBarra+6][75*compBarra-3] = 255
			grafico[50*compBarra+6][75*compBarra-2] = 255
			grafico[50*compBarra+6][75*compBarra-1] = 255
			grafico[50*compBarra+6][75*compBarra] = 255
			grafico[50*compBarra+6][75*compBarra+1] = 255
			grafico[50*compBarra+6][75*compBarra+2] = 255
			grafico[50*compBarra+6][75*compBarra+3] = 255

			if forcas[k] < 0:
				grafico[50*compBarra+4][75*compBarra-2] = 255
				grafico[50*compBarra+5][75*compBarra-3] = 255
				grafico[50*compBarra+6][75*compBarra-4] = 255
				grafico[50*compBarra+7][75*compBarra-3] = 255
				grafico[50*compBarra+8][75*compBarra-2] = 255
				forcas[k] *= -1
			else:
				grafico[50*compBarra-8][75*compBarra-2] = 255
				grafico[50*compBarra-7][75*compBarra-3] = 255
				grafico[50*compBarra-6][75*compBarra-4] = 255
				grafico[50*compBarra-5][75*compBarra-3] = 255
				grafico[50*compBarra-4][75*compBarra-2] = 255

		forcaDecomposta = []
		while forcas[k] != 0:
			numero = forcas[k]%10
			forcas[k] = (forcas[k] - numero)// 10
			forcaDecomposta.insert(0, numero)
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[k], compBarra, grafico, j+1, 0)
		if j == len(forcaDecomposta)-1:
			plotNumeros('m', posicao[k], compBarra, grafico, j+2, 0)
	return grafico

	
def plotEngaste(grafico, compBarra):
	grafico[50*compBarra-1][25*compBarra] = 255
	grafico[50*compBarra-2][25*compBarra] = 255
	grafico[50*compBarra-3][25*compBarra] = 255
	grafico[50*compBarra][25*compBarra] = 255
	grafico[50*compBarra+1][25*compBarra] = 255
	grafico[50*compBarra+2][25*compBarra] = 255
	grafico[50*compBarra+3][25*compBarra] = 255

	grafico[50*compBarra-1][25*compBarra-3] = 255
	grafico[50*compBarra-2][25*compBarra-2] = 255
	grafico[50*compBarra-3][25*compBarra-1] = 255

	grafico[50*compBarra][25*compBarra-1] = 255
	grafico[50*compBarra+1][25*compBarra-2] = 255
	grafico[50*compBarra+2][25*compBarra-3] = 255

	grafico[50*compBarra+3][25*compBarra-1] = 255
	grafico[50*compBarra+4][25*compBarra-2] = 255
	grafico[50*compBarra+5][25*compBarra-3] = 255

	return grafico
		
def plotApoioSimples(grafico, orientacao, posicao, compBarra):
	grafico[50*compBarra+1][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+1][25*compBarra + 50*posicao-1] = 255

	grafico[50*compBarra+2][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao-2] = 255

	grafico[50*compBarra+3][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-3] = 255

	grafico[50*compBarra+4][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-3] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+4] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-4] = 255

	grafico[50*compBarra+6][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-3] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+4] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-4] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+5] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-5] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+6] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-6] = 255

	grafico[50*compBarra+1][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao] = 255
	
	return grafico
def plotApoioDuplo(grafico, orientacao, posicao, compBarra):
	grafico[50*compBarra+1][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+1][25*compBarra + 50*posicao-1] = 255

	grafico[50*compBarra+2][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao-2] = 255

	grafico[50*compBarra+3][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao-3] = 255

	grafico[50*compBarra+4][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-3] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao+4] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao-4] = 255

	grafico[50*compBarra+5][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao-3] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao+4] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao-4] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao+5] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao-5] = 255

	grafico[50*compBarra+6][25*compBarra + 50*posicao+1] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-1] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+2] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-2] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+3] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-3] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+4] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-4] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+5] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-5] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao+6] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao-6] = 255

	grafico[50*compBarra+1][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+2][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+3][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+4][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+5][25*compBarra + 50*posicao] = 255
	grafico[50*compBarra+6][25*compBarra + 50*posicao] = 255

	return grafico

def plotForcaX(forcas, grafico, posicao, compBarra):
	for i in range(0, len(forcas)):
		if posicao[i] == 0:
			if forcas[i] < 0:
				grafico[50*compBarra][25*compBarra+1] = 255	
				grafico[50*compBarra][25*compBarra+2] = 255
				grafico[50*compBarra][25*compBarra+3] = 255
				grafico[50*compBarra][25*compBarra+4] = 255	
				grafico[50*compBarra][25*compBarra+5] = 255
				grafico[50*compBarra][25*compBarra+6] = 255	
				grafico[50*compBarra][25*compBarra+7] = 255

				grafico[50*compBarra-1][25*compBarra] = 255
				grafico[50*compBarra-2][25*compBarra+1] = 255
				grafico[50*compBarra+1][25*compBarra] = 255
				grafico[50*compBarra+2][25*compBarra+1] = 255
				grafico[50*compBarra][25*compBarra-1] = 255
				forcas[i] *= -1
			else: 
				grafico[50*compBarra][25*compBarra-1] = 255
				grafico[50*compBarra][25*compBarra-2] = 255	
				grafico[50*compBarra][25*compBarra-3] = 255
				grafico[50*compBarra][25*compBarra-4] = 255
				grafico[50*compBarra][25*compBarra-5] = 255	
				grafico[50*compBarra][25*compBarra-6] = 255
				grafico[50*compBarra][25*compBarra-7] = 255

				grafico[50*compBarra-1][25*compBarra-2] = 255
				grafico[50*compBarra+1][25*compBarra-2] = 255
				grafico[50*compBarra-2][25*compBarra-3] = 255
				grafico[50*compBarra+2][25*compBarra-3] = 255
		else:
			if forcas[i] < 0:
				grafico[50*compBarra][75*compBarra] = 255
				grafico[50*compBarra][75*compBarra+1] = 255	
				grafico[50*compBarra][75*compBarra+2] = 255
				grafico[50*compBarra][75*compBarra+3] = 255
				grafico[50*compBarra][75*compBarra+4] = 255	
				grafico[50*compBarra][75*compBarra+5] = 255
				grafico[50*compBarra][75*compBarra+6] = 255

				grafico[50*compBarra-1][75*compBarra] = 255
				grafico[50*compBarra-2][75*compBarra+1] = 255
				grafico[50*compBarra+1][75*compBarra] = 255
				grafico[50*compBarra+2][75*compBarra+1] = 255
				grafico[50*compBarra][75*compBarra] = 255
				forcas[i] *= -1
			else: 
				grafico[50*compBarra][75*compBarra] = 255
				grafico[50*compBarra][75*compBarra+1] = 255	
				grafico[50*compBarra][75*compBarra+2] = 255
				grafico[50*compBarra][75*compBarra+3] = 255
				grafico[50*compBarra][75*compBarra+4] = 255	
				grafico[50*compBarra][75*compBarra+5] = 255
				grafico[50*compBarra][75*compBarra+6] = 255

				grafico[50*compBarra-1][75*compBarra+6] = 255
				grafico[50*compBarra-2][75*compBarra+5] = 255
				grafico[50*compBarra+1][75*compBarra+6] = 255
				grafico[50*compBarra+2][75*compBarra+5] = 255
				grafico[50*compBarra][75*compBarra+7] = 255

		forcaDecomposta = []
		while forcas[i] != 0:
			numero = forcas[i]%10
			forcas[i] = (forcas[i] - numero)// 10
			forcaDecomposta.insert(0, numero)
		for j in range(0, len(forcaDecomposta)):
			plotNumeros(forcaDecomposta[j], posicao[i], compBarra, grafico, j-1, 0)
		if j == len(forcaDecomposta)-1:
			plotNumeros('n', posicao[i], compBarra, grafico, j, 0)

	return grafico

def plotNumeros(num, posicao, compBarra, grafico, qtd, posicaox):
	if num == 0:
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	if num == 1:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255

		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	if num == 2:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	elif num == 3:
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	elif num == 4:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
	elif num == 5:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][35*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[10*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[10*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[10*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[10*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[10*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
	elif num == 6:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 25*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 25*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 25*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 25*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 25*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 25*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 25*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 25*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 25*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 25*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 25*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 25*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd] = 255
	elif num == 7:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[15*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[15*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

	elif num == 8:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		
	elif num == 9:
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
	elif num == 'n':
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255

		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+6+7*qtd+3] = 255
	elif num == 'm':
		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+1+7*qtd+3] = 255

		grafico[50*compBarra-11+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+7+7*qtd+3] = 255

		grafico[50*compBarra-10+posicaox][25*compBarra + 50*posicao+2+7*qtd+3] = 255
		grafico[50*compBarra-9+posicaox][25*compBarra + 50*posicao+3+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+4+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+5+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+6+7*qtd+3] = 255

		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+9+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+10+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+11+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+12+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+13+7*qtd+3] = 255
		grafico[50*compBarra-8+posicaox][25*compBarra + 50*posicao+14+7*qtd+3] = 255

		grafico[50*compBarra-7+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255
		grafico[50*compBarra-6+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255
		grafico[50*compBarra-5+posicaox][25*compBarra + 50*posicao+15+7*qtd+3] = 255

	return grafico
def soma(vetor):
	soma = 0
	for x in vetor:
		soma += x 
	return soma

def calculaReacoes(forcas, apoios, posicao):
	if forcas[0] != [0]:
		forcasX= forcas[0]
	else:
		forcasX = 0
	
	if forcas[1] != [0]:
		forcasY = forcas[1]
	else:
		forcasY = 0

	if forcas[2] != [0]:
		momentos = forcas[2]
	else:	
		momentos = 0


	if apoios[0] != [0]:
		apoiosSimples = apoios[0]
	else:
		apoiosSimples = 0
	
	if apoios[1] != [0]:
		apoiosDuplo = apoios[1]
	else:
		apoiosDuplo = 0

	if apoios[2] != [0]:
		engastes = apoios[2]
	else:	
		engastes = 0

	qtdVary, qtdVarx, qtdVarM = 0, 0, 0
	if engastes != 0:
		qtdVary += len(engastes)
		qtdVarx += len(engastes)
		qtdVarM += len(engastes)
	if apoiosDuplo != 0:
		qtdVary += len(apoiosDuplo)
		qtdVarx += len(apoiosDuplo)

	if apoiosSimples != 0:
		qtdVary += len(apoiosSimples)


	resultX = -1*soma(forcasX)
	resultM = -1*soma(momentos)
	resultY = -1*soma(forcasY)

	if qtdVary != 1:

		apoiosY = np.zeros((1,qtdVary))

		apoiosMomentos = np.zeros((1,qtdVary))
		for i in range (qtdVary):
			apoiosMomentos[0][i] = posicao[3][i]
			apoiosY[0][i] = 1
		coefs = np.zeros((2, qtdVary))
		coefs[0], coefs[1] = apoiosY, apoiosMomentos
		results = np.zeros((2, qtdVary))
		results[0], results[1] = resultY, resultM

		print(coefs)

		Y = np.dot(np.linalg.inv(coefs), results)

		return resultX, Y, resultM

	return resultX, resultY, resultM

def plot(compBarra, forcas, posicao):
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
		grafico[50*compBarra-1][x] = 255
		grafico[50*compBarra][x] = 255
		grafico[50*compBarra+1][x] = 255
	#grafico = plotEngaste(grafico, compBarra)
	apoios = [[1],[1],[0]]
	posiApoios = [3, 4, 0]
	posicao.append(posiApoios)
	fx, fy, fm = calculaReacoes(forcas, apoios, posicao)
	forcas[0].append(fx)
	posicao[0].append(posicao[3][1])

	forcas[1].append(fy[0])
	posicao[1].append(posicao[3][0])

	forcas[1].append(fy[1])
	posicao[1].append(posicao[3][1])

	forcas[2].append(fm)
	posicao[2].append(0)

	#grafico = plotApoioSimples(grafico, 1, 3, compBarra)
	#grafico = plotApoioDuplo(grafico, 1, 4, compBarra)
	grafico = plotForcaY(forcas[1], grafico, posicao[1], compBarra)
	grafico = plotForcaX(forcas[0], grafico, posicao[0], compBarra)
	grafico = plotMomento(forcas[2], grafico, posicao[2], compBarra)

	for i in range (0, 100*compBarra):
		for j in range(0, 100*compBarra):
			plotGrafico.write(str(grafico[i][j])+' ')
		plotGrafico.write('\n')
	plotGrafico.close()

def main():
	tamanhoBarra = 5
	orientacaoBarra = 'x'
	forcas = []
	forcasx = []
	forcasy = []
	momentos = []

	forcasx.append(1)

	forcasy.append(-12)
	forcasy.append(10)
	forcasy.append(9)
		
	momentos.append(-2)

	forcas.append(forcasx)
	forcas.append(forcasy)
	forcas.append(momentos)

	posicao = []
	posicaox = []
	posicaoy = []
	posicaoMomento = []

	posicaoMomento.append(0)
	posicaoy.append(1)
	posicaoy.append(2)
	posicaoy.append(5)
	posicaox.append(5)

	posicao.append(posicaox)
	posicao.append(posicaoy)
	posicao.append(posicaoMomento)

	plot(tamanhoBarra, forcas, posicao)
	os.system("diagramas.pgm")
	os._exit(0)


main()