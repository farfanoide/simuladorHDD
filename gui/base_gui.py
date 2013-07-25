import os
import sys
import pygame
from pygame.locals import *

class BaseGui():


    _bkg_colour = (0,0,0)

    def __init__(self, base_sfc, rect, padding=(0,0,0,0), color=_bkg_colour):

        self.start_x  = rect[0]
        self.start_y  = rect[1]
        self.width    = rect[2]
        self.height   = rect[3]
        self.base_sfc = base_sfc
        self.padding  = padding
        self.sfc = pygame.Surface((self.width, self.height))
        self.sfc.fill(color)
        self.base_sfc.blit(self.sfc, rect)   
        pygame.display.update(self.sfc.get_rect())

    def initiate_elements(self):
        pass

    def update_sfc(self):
        self.base_sfc.blit(self.sfc, (self.start_x, self.start_y))
        pygame.display.update(self.base_sfc.get_rect())


        
class Button(BaseGui):
    """docstring for Button"""


    def __init__(self, base_sfc, action="", img=""):
        self.action = action
        self.img    = pygame.image.load(img)
        rect        = self.img.get_rect()
        BaseGui.__init__(self, base_sfc, rect)

    def clicked(self, pos):
        if self.size.collidepoint(pos):
            return True
        else:
            return False
    def update_sfc(self):
        self.base_sfc.blit(self.img, (self.start_x, self.start_y))
        pygame.display.update(self.base_sfc.get_rect())

class Menu(BaseGui):


    def __init__(self, base_sfc, rect, color, buttons, axis):
        BaseGui.__init__(self, base_sfc, rect, color)
        self.initiate_elements(buttons)
        self.populate_sfc(axis)


    # def instantiate_buttons(self, buttons):
    def initiate_elements(self, buttons):
        self.buttons = []
        for button in buttons:
            b = Button(self.sfc, button['action'], button['img'])
            self.buttons.append(b)

    def populate_sfc(self, axis=True, step=20):
        # self.instantiate_buttons(buttons)
        # axis = True  -> x
        # axis = False -> y
        padding = step
        if axis:
            for button in self.buttons:
                button.start_x = padding
                button.start_y = 0
                button.update_sfc()
                padding += button.img.get_width()+step
        else:
            for button in self.buttons:
                button.start_x = 0
                button.start_y = padding
                button.update_sfc()
                padding += button.img.get_height()+step
        self.update_sfc()

# class Main(object):

#     def __init__(self, size):
#         self.screen = pygame.display.set_mode(screen_size)
#         self.screen.fill(black)
#         pygame.display.flip()


#     def update_elements(self, sfc):
#         pygame.display.update(sfc)

#     def initiate_elements(self):
#         menusize = (0, 0, self.screen.get_width(), self.screen.get_height()/8)
#         self.menu = Menu(self.screen, menusize, white)    
        # self.update_elements(self.menu)


