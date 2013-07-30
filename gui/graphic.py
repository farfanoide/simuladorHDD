import os
import sys
import pygame
from pygame.locals import *
from base_gui import BaseGui


class Graphic(BaseGui):
    """Class wich represents the graph area of the screen"""

    def __init__(self, base_sfc, rect):
        super(Graphic, self).__init__(base_sfc, rect)
    def __init__(self, rect, bkg_colour, grid_width, pad=20):
        # self.bkg_colour = bkg_colour
        # self.rect       = rect
        # self.ax_x       = self.rect[0]
        # self.ax_y       = self.rect[1]
        # self.width      = self.rect[2]
        # self.height     = self.rect[3]
        # self.padding    = pad
        #This surface is the graph area with contains the grid with it's labels.
        self.canvas_sfc = pygame.Surface((self.width, self.height))
        self.canvas_sfc.fill(self.bkg_colour)
        ##      Setting the grid
        #   x_coor is the horizontal corrdinate for the grid to be centered
        x_coor = (self.width - grid_width) / 2
        self.grid_rect = (x_coor, self.padding, grid_width,
                self.height - 2 * self.padding -1)
        # Graph surface wich will contain grid + lines
        self.graphic_sfc = pygame.Surface((self.grid_rect[2], self.grid_rect[3]))
        self.graphic_sfc.fill(self.bkg_colour)

    def draw_grid(self, hspacing=0, vspacing=0, gridColour=(0, 0, 0)):
        """ Draws the grid of the graphic"""
        # Let's draw the contour of the graphic
        self.graphic_sfc.fill(self.bkg_colour)
        pygame.draw.rect(self.graphic_sfc, gridColour, (0,0,self.grid_rect[2],self.grid_rect[3]), 3)
        # Now the horizontal lines
        if hspacing:
            for i in range(hspacing, self.grid_rect[2], hspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    i, 0), (i , self.grid_rect[3]))
        # Finally vertical lines
        if vspacing:
            for i in range(vspacing, self.grid_rect[2], vspacing):
                pygame.draw.aaline(self.graphic_sfc, gridColour, (
                    0,  i), (self.grid_rect[0], i))
        self.canvas_sfc.blit(self.graphic_sfc,self.grid_rect)
                
    def label_grid(self, hspacing):
        """Draws the label of the graphic."""
        pygame.font.init()
        grid_ax_x   = self.grid_rect[0] 
        grid_ax_y   = self.grid_rect[1]
        grid_width  = self.grid_rect[2]
        grid_height = self.grid_rect[3]
        for i in range(0, grid_width, hspacing):
            label = pygame.font.SysFont(None, 20)
            label_sfc = label.render(str(i), True, (0, 0, 0))
            # Needed to center the label to the desired coordinate
            half_width = label_sfc.get_width()/2
            self.canvas_sfc.blit(label_sfc, (grid_ax_x + i - half_width, 0))


    def draw_graphic(self, coordinates, img=''):
        """
        this function takes the coordinates given by any algorithm and draws them in the grid

        Keyword arguments:
        coordinates (list) -- List of tuples in the form (x, y)
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

        self.canvas_sfc.blit(self.graphic_sfc,self.grid_rect)
            