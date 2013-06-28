import os,sys,pygame
from pygame.locals import *
from graphics import Graphics
#from pimb import pimb

#inicio pygame
pygame.init()
screen = pygame.display.set_mode((1024,702))
screen.fill((150,150,150))
#creamos superficie grafico
g = Graphics((1024,468),(255,255,255))
g.print_leyends('SSTF','345', True)
g.print_graphic()
g.print_reqs_attended()	
screen.blit(g.graphic_screen,(0,234))
pygame.display.flip()


while True:
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
#			pygame.register_quit(pimb.pimb()) ;) 
			pygame.quit()
			sys.exit()
	