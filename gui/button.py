import pygame
from base import BaseGui
class Button(BaseGui):
    """
    Button class.
    
    img (Surface)   -- Image
    obj (object)    -- object onto wich action will be applied
    action (string) -- action to be applied 

    """

    def __init__(self, base_sfc, action="", obj="", img=""):
        self.img    = pygame.image.load(img).convert()
        self.action = action
        self.obj    = obj
        super(Button, self).__init__(base_sfc, self.img.get_rect())

    def update_sfc(self):
        self.base_sfc.blit(self.img, (self.rect.x, self.rect.y))

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
