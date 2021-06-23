import pygame,random,sys
from pygame.locals import *

class Main():
	def __init__(self):

		arquivo = open("log.txt",'a')
		nome = input("Digite o seu nome: ")
		email = input("Digite o seu email: ")
		arquivo.write("Usuario: "+nome+", "+"Email: "+email+"\n")
		arquivo.close()

		pygame.init()
		pygame.display.set_caption("Jogo")
		screen = pygame.display.set_mode((1000,600))
		clock = pygame.time.Clock()
	
		self.fundo = pygame.image.load('imagens/fundo2.png')
		vogais = []
		consoantes = []
		posicaoXv = [random.randint(0,50),random.randint(100,300),random.randint(310,450),random.randint(480,600),random.randint(650,700)]
		posicaoYv = [0,0,0,0,0]
		velocidadesv = [1,4,3,5,2]

		for n in range(1,6):
			vogais.append(pygame.image.load("imagens/vogal"+str(n)+".png"))
		for n in range(1,6):
			consoantes.append(pygame.image.load("imagens/consoante"+str(n)+".png"))

		while True:
			screen.fill((0,0,0))
			screen.blit(self.fundo,(0,0))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			#fisica das letras e verifica colisao com a tela
			for n in range(0,5):
				posicaoYv[n] = posicaoYv[n] + velocidadesv[n]
				if posicaoYv[n] >= 650:
					posicaoYv[n] = 0

			#mostra na tela as vogais e consoantes
			for n in range(0,5):
				screen.blit(vogais[n],(posicaoXv[n],posicaoYv[n]))

			pygame.display.update()
			clock.tick(60)

if __name__=="__main__":
	Main()
