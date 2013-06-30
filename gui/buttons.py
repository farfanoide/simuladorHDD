import pygame
from pygame.locals import *

class BaseButton():


    def __init__(self, obj_class, action, pos, img='img/button_small.png'):
        self.img = pygame.image.load(img)
        # self.img_active = img_act
        self.rect = (pos[0], pos[1], self.img.get_width(), self.img.get_height())
        self.obj_class = obj_class
        self.action = action

    def executeAction(self):
        action = getattr(self.obj_class, self.action)
        if action:
            return action()
        else:
            print "no action defined"