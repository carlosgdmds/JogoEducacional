import pygame
def MostrarPlacar(pontos,erros,screen):
	pygame.font.init()
	fontesys = pygame.font.SysFont(None, 50)
	texto = fontesys.render("Clique nas vogais para pontuar",1,(255,255,255))
	texto1 = fontesys.render("Pontos: "+str(pontos),1,(255,255,255))
	texto2 = fontesys.render("Erros: "+str(erros),1,(255,255,255))
	screen.blit(texto,(250,5))
	screen.blit(texto1, (10,80))
	screen.blit(texto2, (830,80))
