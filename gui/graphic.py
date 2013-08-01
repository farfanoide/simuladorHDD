import pygame
from pygame.locals import *
from gui.base import BaseGui


class Graphic(BaseGui):
    """Class wich represents the graph area of the screen"""

    def __init__(self, base_sfc, rect, reqs):
        super(Graphic, self).__init__(base_sfc, rect)
        self.coordinates = self.__calculate_coordinates(reqs)
        # self.draw_grid()
        # self.label_grid()
        # self.draw_graphic(coordinates, img='img/req.png')

    def __calculate_vertical_step(self, requirements):
        """Calculates distance between each requirement based on height available and amount of requirements."""

        reqs_quantity = 0
        for reqs in requirements:
            if reqs:
                print reqs
                reqs_quantity += len(reqs)

        height = self.get_height() - self.get_padding_top() - self.get_padding_bottom()
        step = int(height / reqs_quantity)
        return step

    def __calculate_coordinates(self, requirements):
        """Calculates coordinates for the graphic according to amount of requirements and height available."""

        step = self.__calculate_vertical_step(requirements)
        coordinates = ([],[],[])
        i = self.get_padding_top()
        for x in range(len(requirements)):
            try:
                for req in requirements[x]:
                    coordinate = ((req, i))
                    i += step
                    coordinates[x].append(coordinate)
            except IndexError:
                pass
        return coordinates

    def draw_grid(self, hspacing=0, vspacing=0):
        """ Draws the grid of the graphic"""

        # Let's draw the contour of the graphic
        self.draw_surround_rect()
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
        Takes the coordinates given by any algorithm and draws them in the grid

        Keyword arguments:
        coordinates (list) -- List of tuples in the form (x, y)
        """
        for x in range(len(coordinates)):
            if coordinates[x]:
                try:
                    if x:
                        color = _blue
                        if coordinates[x-1] and x == 1:
                            pygame.draw.aaline(self, color, coordinates[x-1][-1], coordinates[x][0], True)
                    else:
                        color = _red
                    pygame.draw.aalines(self, (color, False, coordinates[x], True))
                except ValueError:
                    try:
                        color = _blue if x else _red
                        pygame.draw.aaline(self, color, coordinates[x][-1],coordinates[x+1][0],True)
                    except IndexError:
                        pass
                if not img:
                    for element in coordinates[x]:
                        color = _green if x else _red
                        pygame.draw.circle(self, color, element, 4)
                else:
                    image_sfc = pygame.image.load(img).convert()
                    for coor in coordinates[x]:
                        self.blit(image_sfc, coor)

    def print_canvas(self):
        self.graphic.draw_grid(50)
        self.graphic.label_grid(50) 
        self.graphic.canvas_sfc.blit(self.graphic.graphic_sfc,self.graphic.grid_rect)
        self.graphic_screen.blit(self.graphic.canvas_sfc, (0,0))

    def print_graphic(self, list_reqs):
        self.print_canvas()
        self.graphic.draw_graphic(self.__calculate_coordinates(list_reqs))
        self.graphic_screen.blit(self.graphic.canvas_sfc,(0,0))