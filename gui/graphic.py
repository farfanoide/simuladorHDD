import os
import sys
import pygame
from pygame.locals import *
from base_gui import BaseGui


class Graphic(BaseGui):
    """Class wich represents the graph area of the screen"""

    def __init__(self, base_sfc, rect, coordinates):
        super(Graphic, self).__init__(base_sfc, rect)
        self.draw_grid()
        self.label_grid()
        self.draw_graphic(coordinates, img='img/req.png')

    def draw_grid(self, hspacing=0, vspacing=0, gridColour=(0, 0, 0)):
        """ Draws the grid of the graphic"""
        # Let's draw the contour of the graphic
        self.graphic_sfc.fill(self._bkg_colour)
        pygame.draw.rect(self, self._fg_color, (0, 0, self.get_width(), self.get_height()), 2)
        # Now the horizontal lines
        if hspacing:
            for i in range(hspacing, self.get_width(), hspacing):
                pygame.draw.aaline(self, self._fg_color, (i, 0), (i , self.get_height()))
        # Finally vertical lines
        if vspacing:
            for i in range(vspacing, self.get_width(), vspacing):
                pygame.draw.aaline(self, self._fg_color, (0,  i), (self.get_width(), i))
        self.update_sfc()
                
    def label_grid(self, hspacing):
        """Draws the label of the graphic."""

        pygame.font.init()
        label = pygame.font.SysFont(Ubuntu, 20)

        for i in range(0, self.get_width(), hspacing):
            label_sfc = label.render(str(i), 0, self._fg_color)
            # Needed to center the label to the desired coordinate
            center = (self.rect.x + i) - (label_sfc.get_width() / 2)
            self.blit(label_sfc, (center, 0))


    def draw_graphic(self, coordinates, img=''):
        """
        this function takes the coordinates given by any algorithm and draws them in the grid

        Keyword arguments:
        coordinates (list) -- List of tuples inget_width(), y)
        """
       print coordinates
        for x in range(len(coordinates)):
            if coordinates[x]:
                try:
                    if x:
                        pygame.draw.aalines(self.graphic_sfc,(0,0,255),False,coordinates[x],True)
                        if coordinates[x-1] and x == 1:
                            pygame.draw.aaline(self.graphic_sfc,(0,0,255),coordinates[x-1][-1],coordinates[x][0],True)
                    else:
                        pygame.draw.aalines(self.graphic_sfc,(255,0,0),False,coordinates[x],True)
                except ValueError:
                    try:
                        if x:
                            color = (0,0,255)
                        else:
                            color = (255,0,0)
                        pygame.draw.aaline(self.graphic_sfc, color, coordinates[x][-1],coordinates[x+1][0],True)
                    except IndexError:
                        pass
                if not img:
                    for element in coordinates[x]:
                        if x:
                            pygame.draw.circle(self.graphic_sfc,(0,255,0),element,4)
                        else:
                            # Different colour for page faults
                            pygame.draw.circle(self.graphic_sfc,(255,0,0),element,4)
                else:
                    image_sfc = pygame.image.load(img)
                    for element in coordinates[x]:
                        self.graphic_sfc.blit(image_sfc,element)

        self.canvas_sfc.blit(self.graphic_sfc,self.grid_rect)
            