import os,sys,pygame
from pygame.locals import *
from buttons import BaseButton


class SetUpScreen():

	def __init__(self, screen, obj):
		self.screen = screen
		self.screen.fill((255,0,0))
		self.lote = obj
		self.buttons = []
		self.buttons.append(BaseButton(101, (50,50),  obj_class = self, action = "switchSelect", img="gui/img/button_small.png"))
		self.selected = True

	def showScreen(self):
		self.screen.fill((255,0,0))
		for button in self.buttons:
			self.screen.blit(button.img, button.pos)
		pygame.display.update()

	def switchSelect(self):
		self.selected = not self.selected

class AlgorithmScreen():

	def __init__(self, screen,obj):
		self.screen = screen
		self.screen.fill((0,0,255))
		self.buttons = []
		self.lote = obj
		self.selected = False
		self.buttons.append(BaseButton(101, (10,600), obj_class = self, action = "switchSelect", img="gui/img/button.png"))
		self.buttons.append(BaseButton(2, (10,10), obj_class = self.lote, action = "executeLOOK", img = "gui/img/LOOK.jpg"))
		self.buttons.append(BaseButton(3, (10,70), obj_class = self.lote, action = "executeCLOOK", img ="gui/img/CLOOK.jpg"))
		self.buttons.append(BaseButton(4, (10,130), obj_class = self.lote, action = "executeCSCAN", img ="gui/img/CSCAN.jpg"))
		self.buttons.append(BaseButton(5, (10,190), obj_class = self.lote, action = "executeSCAN", img ="gui/img/SCAN.jpg"))
		self.buttons.append(BaseButton(6, (10,250), obj_class = self.lote, action = "executeFCFS", img ="gui/img/FCFS.jpg"))
		self.buttons.append(BaseButton(7, (10,310), obj_class = self.lote, action = "executeSSTF", img ="gui/img/SSTF.jpg"))
	
	def showScreen(self):
		self.screen.fill((0,0,255))
		for button in self.buttons:
			self.screen.blit(button.img, button.pos)
		pygame.display.update()

	def switchSelect(self):
		self.selected = not self.selected