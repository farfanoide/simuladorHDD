from gui.base import BaseGui
from pygame import *

class Message(BaseGui):

    def __init__(self, base_sfc, rect, color):
        super(Message, self).__init__(base_sfc, rect, color=color)


    def print_message(self, message):
        """Prints a message on screen"""
        pygame.font.init()
        font = pygame.font.SysFont(None,20)
        y = self.rect.y
        for line in message:
            m = font.render(line, True, self._fg_color)
            base_sfc.blit(m,(self.rect-x, y + m.get_height()))
            y += m.get_height()
        self.update_sfc()