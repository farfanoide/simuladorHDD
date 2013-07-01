import os
import sys
import pygame
from pygame.locals import *


class Graphic():

    def __init__(self, rect, bkg_colour, pad=20):
        self.ax_x = rect[0]
        self.ax_y = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.padding = pad
        self.graphic_sfc = pygame.Surface((self.width, self.height))
        self.graphic_sfc.fill(bkg_colour)
        #just for debuggin purpose. Uncoment to see the size of the surface
        #pygame.draw.rect(self.graphic_sfc,(0,0,0),rect,1)

    def draw_grid(self, graph_width, hspacing=0, vspacing=0, gridColour=(0, 0, 0), center = True):
        # if Center = True grid will be x centered
        if center:
            x_coor = (self.width - graph_width) / 2
        rect = (x_coor, self.padding, graph_width,
                self.height - 2 * self.padding - 1)
        # Let's draw the contour of the graphic
        pygame.draw.rect(self.graphic_sfc, gridColour, rect, 2)
        # Now the horizontal lines
        if hspacing:
            for i in range(hspacing, graph_width, hspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    i + x_coor, self.padding), (i + x_coor, self.height - self.padding))
        # Finally vertical lines
        if vspacing:
            for i in range(vspacing, graph_width, vspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    self.padding, self.padding + i), (self.padding + graph_width, self.padding + i))
        return rect

    def label_grid(self, hspacing, grid_coor):
        pygame.font.init()
        grid_ax_x   = grid_coor[0] 
        grid_ax_y   = grid_coor[1]
        grid_width  = grid_coor[2]
        grid_height = grid_coor[3]
        for i in range(0, grid_width, hspacing):
            label = pygame.font.SysFont(None, 20)
            label_sfc = label.render(str(i), True, (0, 0, 0))
            # Needed to center the label to the desired coordinate
            half_width = label_sfc.get_width()/2
            self.graphic_sfc.blit(label_sfc, (grid_ax_x + i - half_width, 0))
            print i


    def draw_graphic(self, coordinates, img=''):
        """this function takes the coordinates given by any algorithm and draws them in the grid"""
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
                            pygame.draw.aaline(self.graphic_sfc,(0,0,255),coordinates[x][-1],coordinates[x+1][0],True)
                        else:
                            pygame.draw.aaline(self.graphic_sfc,(255,0,0),coordinates[x][-1],coordinates[x+1][0],True)
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
                                    
            