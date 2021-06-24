import pygame,random,sys
from pygame.locals import *
from verifica import VerificaColisao, VerificaVencedor
from textos import MostrarPlacar
class Main():
	def __init__(self):

		arquivo = open("log.txt",'a')
		nome = input("Digite o seu nome: ")
		email = input("Digite o seu email: ")
		arquivo.write("Usuario: "+nome+", "+"Email: "+email+"\n")
		arquivo.close()

		pygame.init()
		pygame.display.set_caption("Jogo Educacional ")
		screen = pygame.display.set_mode((1000,600))
		clock = pygame.time.Clock()
	
		self.fundo = pygame.image.load('imagens/fundo.png')
		vogais = []
		consoantes = []
		#x e velocidades das vogais
		self.posicaoXv = [random.randint(0,50),random.randint(100,300),random.randint(310,450),random.randint(480,600),random.randint(650,700)]
		self.velocidadesv = [1,4,3,5,2]

		#x e velocidades das consoantes
		self.posicaoXc = [random.randint(50,100), random.randint(200,250),random.randint(450,500),random.randint(500,600),random.randint(680,750)]
		self.velocidadesc = [2,5,3,4,6]

		#posicao Y
		self.posicaoYv, self.posicaoYc = [0,0,0,0,0],[0,0,0,0,0]

		self.pontos = 0
		self.erros = 0

		for n in range(1,6):
			vogais.append(pygame.image.load("imagens/vogal"+str(n)+".png"))
			consoantes.append(pygame.image.load("imagens/consoante"+str(n)+".png"))

		while True:
			screen.fill((0,0,0))
			screen.blit(self.fundo,(0,0))
		
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
						if event.button == 1:
							self.pontos,self.erros,self.posicaoYv, self.posicaoYc,self.posicaoXv, posicaoXc = VerificaColisao(self.x,self.y, self.posicaoXv, self.posicaoYv, self.posicaoXc, self.posicaoYc,self.pontos,self.erros)

			self.x,self.y = pygame.mouse.get_pos()

			#fisica das letras e verifica colisao com a tela
			for n in range(0,5):
				self.posicaoYv[n] = self.posicaoYv[n] + self.velocidadesv[n]
				self.posicaoYc[n] = self.posicaoYc[n] + self.velocidadesc[n]
				if self.posicaoYv[n] >= 650:
					self.posicaoYv[n] = 0
				if self.posicaoYc[n] >= 650:
					self.posicaoYc[n] = 0
		
			VerificaVencedor(self.pontos,self.erros,screen)

			#mostra na tela as vogais e consoantes
			MostrarPlacar(self.pontos,self.erros,screen)
			for n in range(0,5):
				screen.blit(vogais[n],(self.posicaoXv[n],self.posicaoYv[n]))
				screen.blit(consoantes[n],(self.posicaoXc[n],self.posicaoYc[n]))

			pygame.display.update()
			clock.tick(60)

if __name__=="__main__":
	Main()
