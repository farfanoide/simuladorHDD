import os
import sys
import pygame
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

