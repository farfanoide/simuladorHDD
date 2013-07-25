import pygame

from pygame.locals import *

class BaseButton():


    def __init__(self, idn, pos, obj_class = "", action="", img="gui/img/button_small.png"):
        self.id = idn
        self.pos = pos
        self.img = pygame.image.load(img)
        # self.rect = (pos[0], pos[1], self.img.get_width(), self.img.get_height())
        self.rect = self.img.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.obj_class = obj_class

    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def executeAction(self):
        action = getattr(self.obj_class, self.action)
        if action:
            return action()
        else:
            print "no action defined"



