import pygame
from base import BaseGui
class Button(BaseGui):
    """
    Button class.
    
    img (Surface)   -- Image
    obj (object)    -- object onto wich action will be applied
    action (string) -- action to be applied 

    """

    def __init__(self, base_sfc,id = 0, action="", obj="", img=""):
        try:
            self.img    = pygame.image.load(img).convert_alpha()
        except:
            self.img = pygame.image.load('gui/img/button_small.png').convert_alpha()
        self.action  = action
        self.obj     = obj
        self.id = id
        super(Button, self).__init__(base_sfc, self.img.get_rect())
        self.blit(self.img, (0,0))

    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def executeAction(self):
        action = getattr(self.obj, self.action)
        if action:
            return action()
        else:
            print "No action defined"

    def set_caption(self, text, pos):
        pygame.font.init()
        font = pygame.font.SysFont(None, 30)
        caption = font.render(str(text), True, self._red)
        self.blit(caption, pos)
