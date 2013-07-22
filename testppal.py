import os,sys,pygame
from pygame.locals import *
from gui.guiclasses import *
from simulator import Simulator
# from gui.screen_algorithms import ScreenAlgorithms
##begin
pygame.init()

screen = pygame.display.set_mode((1024,702))
sim = Simulator()
sus = SetUpScreen(screen,sim)
als = AlgorithmScreen(screen,sim)
run = True

while run:
	if sus.selected:
		buttons = sus.buttons
		sus.showScreen()
	else:
		buttons = als.buttons
		als.showScreen()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for button in buttons:
				if button.clicked(pos):
					if button.id <100:
						result = button.executeAction()
						reqs = results[0][0]
						movs = str(results[0][1])
						dire = results[0][2]
					else:
						sus.switchSelect()
		if event.type == pygame.QUIT:
			run = False
		#faster dubugging
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			run = False
pygame.quit()
sys.exit()    


