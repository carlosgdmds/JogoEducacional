import pygame,random,time
def VerificaColisao(x,y,posicaoXv,posicaoYv, posicaoXc, posicaoYc, pontos, erros):
	for n in range(0,5):
		#verifica colisao entre as vogais
		if x >= posicaoXv[n] and x <= posicaoXv[n] + 100 and y >= posicaoYv[n] and y <= posicaoYv[n] + 100:
				pontos +=1
				posicaoYv[n] = -80
				posicaoXv[n] = random.randint(0,750)

		#verifica colisao entre as consoantes
		if x >= posicaoXc[n] and x <= posicaoXc[n] + 100 and y >= posicaoYc[n] and y <= posicaoYc[n] + 100:
				erros +=1
				posicaoYc[n] = -80
				posicaoXc[n] = random.randint(0,750)
	return pontos,erros, posicaoYv, posicaoYc, posicaoXv, posicaoXc

def VerificaVencedor(pontos,erros,screen):
	pygame.font.init()
	fontesys = pygame.font.SysFont(None, 50)
	if pontos >=10:
		texto = fontesys.render("Voce ganhou",1,(255,255,255))
		screen.blit(texto, (350,300))
		pygame.display.update()
		time.sleep(3)
		pygame.quit()
		quit()

	if erros >=5:
		texto = fontesys.render("Voce perdeu",1,(255,255,255))
		screen.blit(texto,(350,300))
		pygame.display.update()
		time.sleep(3)
		pygame.quit()
		quit() 
	
