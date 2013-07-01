import pygame

from pygame.locals import *

class BaseButton(pygame.sprite.Sprite):


    def __init__(self, obj_class, pos, action="", img='gui/img/button_small.png'):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        print self.pos
        self.img = pygame.image.load(img)
        # self.rect = (pos[0], pos[1], self.img.get_width(), self.img.get_height())
        self.rect = self.img.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.obj_class = obj_class
        self.action = action

    def clicked(self, rect):
        if pygame.sprite.collide_rect(self, rect):
            return True
        else:
            return False

    def executeAction(self):
        action = getattr(self.obj_class, self.action)
        if action:
            return action()
        else:
            print "no action defined"