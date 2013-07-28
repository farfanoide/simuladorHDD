import os
import sys
import pygame
import string
from pygame.locals import *

class BaseGui(object):


	_bkg_colour = (0,0,0)

	def __init__(self, base_sfc, rect, padding=(0,0,0,0), color=_bkg_colour):
		print rect
		self.start_x  = rect[0]
		self.start_y  = rect[1]
		self.width    = rect[2]
		self.height   = rect[3]
		self.rect     = rect
		self.base_sfc = base_sfc
		self.padding  = padding
		self.elements = []
		self.sfc = pygame.Surface((self.width, self.height))
		# self.sfc.fill(color)
		self.base_sfc.blit(self.sfc, rect)   
		pygame.display.update(self.sfc.get_rect())
		self.colour = color

	def initiate_elements(self):
		pass

	def update_sfc(self):
		if (self.elements):
			for e in self.elements:
				e.update_sfc()
		self.base_sfc.blit(self.sfc, (self.start_x, self.start_y))
		pygame.display.update(self.base_sfc.get_rect())


		
class Button(BaseGui):
	"""docstring for Button"""


	def __init__(self, base_sfc, action="", img=""):
		self.action = action
		self.img    = pygame.image.load(img)
		rect        = self.img.get_rect()
		# BaseGui.__init__(self, base_sfc, rect)
		super(Button, self).__init__(base_sfc, rect)

	def clicked(self, pos):
		if self.rect.collidepoint(pos):
			return True
		else:
			return False

	def update_sfc(self):
		self.base_sfc.blit(self.img, (self.start_x, self.start_y))
		pygame.display.update(self.base_sfc.get_rect())

class Menu(BaseGui):


	def __init__(self, base_sfc, rect, color, buttons, axis):
		super(Menu, self).__init__(base_sfc, rect, color)
		self.initiate_elements(buttons)
		self.populate_sfc(axis)
		self.update_sfc()


	# def instantiate_buttons(self, buttons):
	def initiate_elements(self, buttons):
		for button in buttons:
			b = Button(self.sfc, button['action'], button['img'])
			self.elements.append(b)

	def populate_sfc(self, axis=True, step=20):
		# self.instantiate_buttons(buttons)
		# axis = True  -> x
		# axis = False -> y
		padding = step
		if axis:
			for button in self.elements:
				button.start_x = padding
				button.start_y = 0
				# button.update_sfc()
				padding += button.img.get_width()+step
		else:
			for button in self.elements:
				button.start_x = 0
				button.start_y = padding
				# button.update_sfc()
				padding += button.img.get_height()+step
		

class Screen(BaseGui):
	"""docstring for Screen"""


	def __init__(self, base_sfc, rect, color, elements):
		super(Screen, self).__init__(base_sfc, rect, color)
		self.elements = elements
		self.selected = True


class InputBox(BaseGui):
	""" Docstring for InputBox"""
	def __init__(self, base_sfc, rect, color):
		super(InputBox, self).__init__(base_sfc, rect, color)
		self.input=[]
		self.inputxt=""
		self.inputlst=[]
		self.line_height = 0
		self.line_cont = 0
		self.ask()
		self.update_sfc()

	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
	 			return event.key
			else:
				pass
# TODO: refactor variable names/
	def display_box(self, message):
	  	"Print a message in a box in the middle of the sfc"
		fontobject = pygame.font.Font(None,18)
		self.line_height=0
		# self.sfc.fill(self.colour)
		pygame.draw.rect(self.sfc, (0,0,0),(0,(self.sfc.get_height() / 2),self.sfc.get_width(),self.sfc.get_height()/2), 0)
		pygame.draw.rect(self.sfc, (255,255,255),(1,(self.sfc.get_height() / 2) +1,self.sfc.get_width()-1, self.sfc.get_height()-1), 1)
		if len(message) != 0:
			for lines in self.inputlst:
				line = fontobject.render(lines, 1, (255, 255, 255))
				self.sfc.blit(line, (0, self.sfc.get_height() / 2 + self.line_height))
				self.line_height += line.get_height()
			line = fontobject.render(message, 1, (255, 255, 255))
			self.sfc.blit(line, (0, self.sfc.get_height() / 2 + self.line_height))
			# pygame.display.flip()
			if line.get_width() > self.sfc.get_width() - 10 :
				self.inputlst.append(message)
				self.line_height =self.line_height + line.get_height()
				return True
			else:
				return False
		

	def ask(self):
		"ask(sfc, question) -> answer"
		pygame.font.init()
		current_string = []
		self.display_box(string.join(current_string,""))
		while 1:
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
				if len(self.inputlst) > 0 and current_string == "":
					self.inputlst.pop()
					current_string = self.inputlst.pop()
				self.display_box(string.join(current_string,""))
			elif inkey == K_RETURN:
				self.inputlst.append(string.join(current_string,""))
				break
			elif inkey <= 127:
				current_string.append(chr(inkey))
				if self.display_box(string.join(current_string,"")):
					# self.inputlst.append(string.join(current_string,""))
					current_string = []
			self.update_sfc()
		print self.inputlst
		# self.inputxt = string.join(current_string,"")
		# return string.join(current_string,"")


