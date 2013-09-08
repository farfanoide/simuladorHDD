from gui.base import BaseGui
import pygame
from pygame.locals import *

class Message(BaseGui):

    def __init__(self, base_sfc, rect, color):
        super(Message, self).__init__(base_sfc, rect, color=color)


    def print_message(self, message):
        """Prints a message on screen"""
        self.fill((0,0,0))
        pygame.font.init()
        font = pygame.font.SysFont(None,20)
        y = self.rect.y
        print y
        for line in message:
            print line
            m = font.render(line, True, (255,255,255))
            print m.get_height()
            self.blit(m,(self.rect.x,y + m.get_height()))
            y += m.get_height()
        self.update_sfc()