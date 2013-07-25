import os
import sys
import pygame
from pygame.locals import *
# pygame.Surface
# var
screen_size = (1000, 640)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
butt_list=[('sometext','img/button.png'),('sometext','img/button.png'),('sometext','img/button.png'),('sometext','img/button.png')]


class BaseGui():

    def __init__(self, base_sfc, rect, color):

        self.start_x = rect[0]
        self.start_y = rect[1]
        self.width   = rect[2]
        self.height  = rect[3]
        self.base_sfc = base_sfc
        self.sfc = pygame.Surface((self.width, self.height))
        self.sfc.fill(color)
        self.base_sfc.blit(self.sfc, rect)   
        pygame.display.update(self.sfc.get_rect())

    def initiate_elements(self):
        pass

    def update_sfc(self):
        self.base_sfc.blit(self.sfc, (self.start_x, self.start_y))


        
class Button(BaseGui):
    """docstring for Button"""
    def __init__(self, text="button", img='img/button.png'):
        self.text = text
        self.img = pygame.image.load(img)
        self.size = self.img.get_rect()

    def clicked(self, pos):
        if self.size.collidepoint(pos):
            return True
        else:
            return False

class Menu(BaseGui):

    # def instantiate_buttons(self, buttons):

    def populate_sfc(self, buttons, axis=True, step=20):
        # self.instantiate_buttons(buttons)
        # axis = True  -> x
        # axis = False -> y
        self.buttons = []
        for button in buttons:
            b = Button(button[0], button[1])
            self.buttons.append(b)
        padding = 0
        if axis:
            for button in self.buttons:
                self.sfc.blit(button.img, (padding, 0))
                padding += button.img.get_width()+step
        else:
            for button in self.buttons:
                self.sfc.blit(button.img, (0, padding))
                padding += button.img.get_width()+step
        self.update_sfc()

class Main(object):

    def __init__(self, size):
        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill(black)
        pygame.display.flip()


    def update_elements(self, sfc):
        pygame.display.update(sfc)

    def initiate_elements(self):
        menusize = (self.screen.get_width(), self.screen.get_height()/8, 0, 0)
        self.menu = Menu(self.screen, menusize, white)    
        # self.update_elements(self.menu)


pygame.init()

m = Main(screen_size)
m.initiate_elements()
m.menu.populate_sfc(butt_list)
pygame.display.flip()
# print screen.get_width()




run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        # print event
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in m.menu.buttons:
                if button.clicked(pos):
                    print button.img.get_clip()
            #         print button.img.get_abs_parent().get_rect()
                    # print super(Button, button).get_rect()
            
            # screen.blit(n.img, (200,200))
            # pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False
        #faster dubugging
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
# pygame.quit()
# sys.exit(), 