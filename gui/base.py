import os
import sys
import pygame
import string
from pygame.locals import *


class BaseGui(pygame.surface.Surface):
    """
    Base class for all graphical elements.
    elements (list) -- List containing subelements.
    padding (list)  -- List representing padding in the order: [top, right, bottom, left]

    """

    # Colors:
    # ----------------
    _bg_color = (31, 34, 39)
    _fg_color = (181, 181, 181)
    _blue     = (0, 0, 255) 
    _red      = (255, 0, 0)
    _green    = (0, 255, 0)

    def __init__(self, base_sfc, rect, padding=[20, 20, 20, 20], color=_bg_color):
        super(BaseGui, self).__init__((rect[2], rect[3]))
        self.rect     = self.get_rect()
        self.rect.x   = rect[0]
        self.rect.y   = rect[1]
        self.base_sfc = base_sfc
        self.padding  = padding
        self.elements = []
        self.fill(color)
        self.update_sfc()

    def initiate_elements(self):
        pass

    def update_sfc(self):
        if self.elements:
            for e in self.elements:
                e.update_sfc()
        self.base_sfc.blit(self, (self.rect.x, self.rect.y))
        pygame.display.update(self.base_sfc.get_rect())
    
    def get_padding_top(self):
        return self.padding[0]
    
    def get_padding_right(self):
        return self.padding[1]
    
    def get_padding_bottom(self):
        return self.padding[2]
    
    def get_padding_left(self):
        return self.padding[3]

    def apply_padding(self):
        """
        Creates Rect based on own (width, height) and adds padding
        self.padding (list) representing [top, right, bottom, left]

        """
        draw_rect = self.get_rect()
        draw_rect[0] += self.get_padding_top()
        draw_rect[1] += self.get_padding_right()
        draw_rect[2] -= self.get_padding_bottom() * 2
        draw_rect[3] -= self.get_padding_left() * 2
        return draw_rect

    def get_center_coor(self):
        dist = self.get_width() + self.get_padding_left() + self.get_padding_right()
        cent = self.base_sfc.get_width() - dist / 2
        return cent

    def draw_surround_rect(self, bkg=_bg_color, fg=_fg_color, padding=True):
        self.fill(bkg)
        if padding:
            rect = self.apply_padding()
        else:
            rect = self.get_rect()
        pygame.draw.rect(self, fg, rect, 1)
