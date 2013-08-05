import pygame
from pygame.locals import *
from gui.base import BaseGui


class Graphic(BaseGui):
    """Class wich represents the graph area of the screen"""

    def __init__(self, base_sfc, rect, color):
        super(Graphic, self).__init__(base_sfc, rect, color=color)

    def __calculate_vertical_step(self, requirements):
        """Calculates distance between each requirement based on height available and amount of requirements."""

        reqs_quantity = 0
        for reqs in requirements:
            if reqs:
                reqs_quantity += len(reqs)

        height = self.get_height() - self.get_padding_top() - self.get_padding_bottom()
        step   = int(height / reqs_quantity)
        return step

    def __calculate_coordinates(self, requirements):
        """Calculates coordinates for the graphic according to amount of requirements and height available."""

        step = self.__calculate_vertical_step(requirements)
        coordinates = ([], [], [])
        i   = self.get_padding_top()
        pad = self.get_padding_left()
        for x in range(len(requirements)):
            try:
                for req in requirements[x]:
                    coordinate = ((req + pad, i))
                    i += step
                    coordinates[x].append(coordinate)
            except IndexError:
                pass
        return coordinates

    def draw_grid(self, hspacing=0, vspacing=0):
        """ Draws the grid of the graphic"""

        # Let's draw the contour of the graphic
        self.draw_surround_rect()
        
        top    = self.get_padding_top()
        right  = self.get_width() - self.get_padding_right()
        bottom = self.get_height() - self.get_padding_bottom()
        left   = self.get_padding_left()
        
        # Now the horizontal lines
        if hspacing:
            for i in range(hspacing, self.get_width() - left, hspacing):
                pygame.draw.aaline(self, self._fg_color, (i+ left, top), (i + left , bottom))
        # Finally vertical lines
        if vspacing:
            for i in range(vspacing, self.get_width(), vspacing):
                pygame.draw.aaline(self, self._fg_color, (left,  i), (right, i))
        # self.update_sfc()
                
    def label_grid(self, hspacing):
        """Draws the label of the graphic."""

        pygame.font.init()
        font  = pygame.font.SysFont(None, 20)
        start = self.get_padding_left()
        right = self.get_width() - self.get_padding_right()
        for i in range(0, right, hspacing):
            label_sfc = font.render(str(i), True, self._fg_color)
            # Needed to center the label to the desired coordinate
            center = i - label_sfc.get_width() / 2 + start
            self.blit(label_sfc, (center, 0))
    
    def __print_req_label(self, font, coor, img_offset=4):

        x, y = coor
        y -= img_offset

        req = str(x - self.get_padding_left())
        req_sfc = font.render(req, True, self._fg_color)

        if x <= 500:
            x += img_offset * 2
        else:
            x -= img_offset * 6
            
        self.blit(req_sfc, (x, y))



    def draw_graphic(self, coordinates, img=''):
        """
        Takes the coordinates given by any algorithm and draws them in the grid

        Keyword arguments:
        coordinates (list) -- List of tuples in the form (x, y)
        """
        for x in range(len(coordinates)):
            if coordinates[x]:
                try:
                    if x:
                        color = self._blue
                        if coordinates[x-1] and x == 1:
                            pygame.draw.aaline(self, color, coordinates[x-1][-1], coordinates[x][0], True)
                    else:
                        color = self._red
                    pygame.draw.aalines(self, color, False, coordinates[x], True)
                except ValueError:
                    try:
                        color = self._blue if x else self._red
                        pygame.draw.aaline(self, color, coordinates[x][-1],coordinates[x+1][0],True)
                    except IndexError:
                        pass

                pygame.font.init()
                font = pygame.font.SysFont(None, 20)
                
                if not img:
                    for coor in coordinates[x]:
                        color = self._green if x else self._red
                        pygame.draw.circle(self, color, coor, 4)
                        self.__print_req_label(font, coor)

                else:
                    img_sfc = pygame.image.load(img).convert_alpha()
                    img_offset = int(img_sfc.get_width() / 2)
                    for coor in coordinates[x]:
                        self.__print_req_label(font, coor, img_offset)
                        self.blit(img_sfc, (coor[0] - img_offset, coor[1] - img_offset))

    def print_graphic(self, reqs):
        coordinates = self.__calculate_coordinates(reqs)
        self.draw_grid(50)
        self.label_grid(50) 
        self.draw_graphic(coordinates, 'gui/img/req.png')
        self.update_sfc()