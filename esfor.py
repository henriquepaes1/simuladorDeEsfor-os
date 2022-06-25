
import numpy as np
import os
def achaPontoMedio(x1, y1, x2, y2):
	return int((x1+x2)/2), int((y1+y2)/2)
def preenche(grafico, maior, m):
	for i in range(len(grafico)):
		for j in range(len(grafico[1])):
			if grafico[i][j] == 11:
				x = 0
				while i + x < 26*maior-1:
					grafico[i+x][j] = 11
					y = 1
					while j+y < (15*m + 22): 
						grafico[i+x][j+y] = 11
						y += 1
					x += 1 

def completaGrafico(grafico, maior, m):
	primeiro = True
	for x in range(10):
		for i in range(len(grafico)):
			for j in range(len(grafico[1])):
				if grafico[i][j] == 11:
					if primeiro == True:
						x1, y1 = i, j
						primeiro = False
					else:
						x2, y2 = i, j
						if abs((x2 - x1)) >=2 and abs((y2 - y1)) >=2:
							xm, ym = achaPontoMedio(x1, y1, x2, y2)
							grafico[xm][ym] = 11
							while abs((x2 - xm)) >=2 and abs((y2 - ym)) >=2:
								xm, ym = achaPontoMedio(xm, ym, x2, y2)
								grafico[xm][ym] = 11

						x1, y1 = i, j

	preenche(grafico, maior, m)

def valorEquacao(a, b, equacao):
	listaResultado = []
	for x in range(a, b+1):
		resultado = 0
		for i in range(len(equacao)):
			resultado += equacao[i]*(x**i)
		listaResultado.append(resultado)
	return listaResultado

def maximoValor(valores):
	maxi = 0
	for x in (valores):
		if abs(x) > maxi:
			maxi = abs(x)
	return round(maxi)

def diagramasSolicitantes(equacoes, inicioCorte, fimCorte):
	momento = valorEquacao(inicioCorte, fimCorte, equacoes[2])
	normal = valorEquacao(inicioCorte, fimCorte, equacoes[1])
	cortante = valorEquacao(inicioCorte, fimCorte, equacoes[0])
	
	maiorMomento = maximoValor(momento)+1
	maiorCortante = maximoValor(cortante)+1
	maiorNormal = maximoValor(normal)+1

	m = fimCorte - inicioCorte+1
	
	graficoCortante = np.zeros((50*maiorCortante, 50*m))
	graficoNormal = np.zeros((50*maiorNormal, 50*m))
	graficoMomento = np.zeros((50*maiorMomento, 50*m))

	plotGraficoCortante = open('cortante.pgm', 'w')
	plotGraficoCortante.write('\n P2 \n')
	plotGraficoCortante.write(str(50*m)+ ' '+str(50*maiorCortante))
	plotGraficoCortante.write('\n 15 \n')

	plotGraficoNormal = open('normal.pgm', 'w')
	plotGraficoNormal.write('\n P2 \n')
	plotGraficoNormal.write(str(50*m)+ ' '+str(50*maiorNormal))
	plotGraficoNormal.write('\n 15 \n')

	plotGraficoMomento = open('momento.pgm', 'w')
	plotGraficoMomento.write('\n P2 \n')
	plotGraficoMomento.write(str(50*m)+ ' '+str(50*maiorMomento))
	plotGraficoMomento.write('\n 15 \n')

	for x in range(22):
		graficoMomento[26*maiorMomento][15*m + x] = 15
		graficoCortante[26*maiorCortante][15*m + x] = 15
		graficoNormal[26*maiorNormal][15*m + x] = 15	
	
	for i in range(0, maiorCortante):
		for j in range(0, m):
			if i == (maiorCortante - cortante[j]):
				graficoCortante[25*maiorCortante + i][15*m + 10*j] = 11

			else:
				graficoCortante[25*maiorCortante + i][15*m + 10*j] = 0

	for i in range(0, maiorMomento):
		for j in range(0, m):
			if i == (maiorMomento - momento[j]):
				graficoMomento[25*maiorMomento + i][15*m + 10*j] = 11

			else:
				graficoMomento[25*maiorMomento + i][15*m + 10*j] = 0
	
	for i in range(0, maiorNormal):	
		for j in range(0, m):
			if i == (maiorNormal - normal[j]):
				graficoNormal[25*maiorNormal + i-1][15*m + 10*j] = 11
			else:
				graficoNormal[25*maiorNormal + i-1][15*m + 10*j] = 0

	completaGrafico(graficoNormal, maiorNormal, m)
	for i in range(len(graficoNormal)):
		for j in range(len(graficoNormal[i])):
			plotGraficoNormal.write(str(graficoNormal[i][j])+' ')
	completaGrafico(graficoMomento, maiorMomento, m)
	for i in range(len(graficoMomento)):
		for j in range(len(graficoMomento[i])):
			plotGraficoMomento.write(str(graficoMomento[i][j])+' ')
	completaGrafico(graficoCortante, maiorCortante, m)
	for i in range(len(graficoCortante)):
		for j in range(len(graficoCortante[i])):
			plotGraficoCortante.write(str(graficoCortante[i][j])+' ')

	plotGraficoCortante.close()
	plotGraficoNormal.close()
	plotGraficoMomento.close()
	os.system("cortante.pgm")
	os.system("normal.pgm")
	os.system("momento.pgm")
	os._exit(0)
equacoes =[[1,1], [1], [0,1,1]]
diagramasSolicitantes(equacoes, 1, 3)
