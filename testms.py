#uses utf-8: encoding
import pygame
import os,sys
from pygame.locals import *
import Vmain
import graphic
pygame.init()

mscreen = Vmain.main_screen(1024,600,(250,250,130),'SuperSimuladorHDD')
mscreen.base()
mscreen.add_button((100,300,100,50),(30,30,30),text = 'boton')
mscreen.add_label((400,100,100,50),'label1', width=5, colour=(100,100,100),rect_colour=(255,0,0))
mscreen.add_button((800,500,50,50),(100,100,100), text='boton2')
mscreen.draw_grid(511,200,25,10)
mscreen.show_screen()

while True:
	events = pygame.event.get()
	
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	


