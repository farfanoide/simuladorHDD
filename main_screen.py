import os,sys
import pygame
from pygame.locals import *

class main_screen:
	
	def __init__(self, width=1024, height=768, colour=(0,0,0), title='titulo'):
		self.size = (width, height)
		self.bkg_colour = colour
		self.Wtitle = title
		self.screen = pygame.display.set_mode(self.size)
		self.screen.fill(self.bkg_colour)
		pygame.display.set_caption(self.Wtitle)
		

		
	
	def add_button(self, coor, colour=(0,0,0), image = '', text='', text_colour =(255,255,255)):
		if (image != ''):
			img = pygame.image.load(image)
			self.buttons.append(self.screen.blit(img,(coor[2],coor[3])))
		else:
			sfc_button = pygame.Surface((coor[2],coor[3]))						#creamos superficie
			pygame.draw.rect(sfc_button,(100,100,100),(0,0,coor[2],coor[3]), 3)	#recuadro
			txt_button = pygame.font.SysFont(None,coor[3]/3)					# tipo texto boton
			sfc_button_txt = txt_button.render(text, True , text_colour) 		#render texto boton
			large=sfc_button_txt.get_width()									#largo del texto
			self.buttons.append(sfc_button.blit(sfc_button_txt,((coor[2]-large)/2,coor[3]/3))) 		#centramos el texto en el boton
			self.screen.blit(sfc_button,coor)

#	def add_label(self, coor, text,text_colour=(0,0,0), colour=(), width=0, rect_colour=(0,0,0)):
#		sfc_label = pygame.Surface ((coor[2],coor[3]))					#creamos superficie
#		if colour!=():													# establece el color de fondo
#			sfc_label.fill(colour)
#		else:
#			sfc_label.fill(self.bkg_colour)
#	
#		if width!=0 :													#width distinto de cero : va con recuadro
#			pygame.draw.rect(sfc_label,rect_colour,(0,0,coor[2],coor[3]),width)
#		txt_label = pygame.font.SysFont(None,coor[3]/3)
#		sfc_label_txt = txt_label.render(text, True , text_colour) 		#render texto
#		large=sfc_label_txt.get_width()									#largo del texto
#		sfc_label.blit(sfc_label_txt,((coor[2]-large)/2,coor[3]/3)) 	#centramos el texto en el label
#		self.screen.blit(sfc_label,coor)
	
	def make_grid(self,width,height,hspacing,vspacing,colour=(0,0,0)):
		grid_sfc = pygame.Surface((width,height))
		grid_sfc.fill(self.bkg_colour)
		pygame.draw.rect(grid_sfc,colour,(0,0,width,height),3)
		for i in range(0,width,vspacing):
			pygame.draw.aaline(grid_sfc,colour,(i,0),(i,height+10),2)
		for j in range(0,height+1,hspacing):
			pygame.draw.aaline(grid_sfc,colour,(0,j),(width+10,j),2)
		self.screen.blit(grid_sfc,(0,0,width,height))
	
	def show_screen(self):
		pygame.display.flip()
