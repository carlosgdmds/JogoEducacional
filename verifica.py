import pygame
def VerificaColisao(x,y,posicaoXv,posicaoYv, posicaoXc, posicaoYc, pontos, erros):
	for n in range(0,5):
		#verifica colisao entre as vogais
		if x >= posicaoXv[n] and x <= posicaoXv[n] + 100 and y >= posicaoYv[n] and y <= posicaoYv[n] + 100:
				print("colidiu com uma vogal")
				pontos +=1
		#verifica colisao entre as consoantes
		if x >= posicaoXc[n] and x <= posicaoXc[n] + 100 and y >= posicaoYc[n] and y <= posicaoYc[n] + 100:
				print("colidiu com uma consoante")
				erros +=1
	return pontos,erros

def VerificaVencedor(pontos,erros):
	if pontos >=10:
		print("ganhou")
		pygame.quit()
		quit()
	if erros >=3:
		print("Voce perdeu")
		pygame.quit()
		quit() 
