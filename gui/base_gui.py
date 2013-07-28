import os
import sys
import pygame
from pygame.locals import *

class BaseGui(pygame.surface.Surface):


    _bkg_colour = (0,0,0)

    def __init__(self, base_sfc, rect, padding=(0, 0, 0, 0), color=_bkg_colour):
        print rect
        super(BaseGui, self).__init__((rect[2], rect[3]))
        self.rect     = self.get_rect()
        self.rect.x   = rect[0]
        self.rect.y   = rect[1]
        self.base_sfc = base_sfc
        self.padding  = padding
        self.elements = []
        self.base_sfc.blit(self, self.rect)   
        pygame.display.update(self.rect)

    def initiate_elements(self):
        pass

    def update_sfc(self):
        if (self.elements):
            for e in self.elements:
                e.update_sfc()
        self.base_sfc.blit(self, (self.rect.x, self.rect.y))
        pygame.display.update(self.base_sfc.get_rect())


        
class Button(BaseGui):
    """docstring for Button"""


    def __init__(self, base_sfc, action="", simulator="", img=""):
        self.img = pygame.image.load(img)
        self.action = action
        self.simulator = simulator
        super(Button, self).__init__(base_sfc, self.img.get_rect())
    
    def update_sfc(self):
        self.base_sfc.blit(self.img, (self.rect.x, self.rect.y))
    
    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def executeAction(self):
        action = getattr(self.simulator, self.action)
        if action:
            return action()
        else:
            print "no action defined"

class Menu(BaseGui):


    def __init__(self, base_sfc, rect, color, buttons, axis):
        super(Menu, self).__init__(base_sfc, rect, color)
        self.initiate_elements(buttons)
        self.populate_sfc(axis)
        self.update_sfc()

    def initiate_elements(self, buttons):
        for button in buttons:
            b = Button(self, button['action'], button['simulator'], button['img'])
            self.elements.append(b)

    def populate_sfc(self, axis=True, step=20):
        # axis = True  -> x
        # axis = False -> y
        padding = step
        if axis:
            for button in self.elements:
                button.rect.x = padding
                button.rect.y = step
                padding += button.get_width()+step
        else:
            for button in self.elements:
                button.rect.x = step
                button.rect.y = padding
                padding += button.get_height()+step
        

class Screen(BaseGui):
    """docstring for Screen"""


    def __init__(self, base_sfc, rect, color, elements):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = True

    def showScreen(self):
        self.screen.fill(self.bkg_colour)
        for button in self.buttons:
            self.screen.blit(button.img, button.pos)
        pygame.display.update()

    def switchSelect(self):
        self.screen.fill(self.bkg_colour)
        self.selected = not self.selected