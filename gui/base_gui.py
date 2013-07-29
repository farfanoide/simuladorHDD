import os
import sys
import pygame
import string
from pygame.locals import *


class BaseGui(pygame.surface.Surface):

    _bkg_colour = (31, 34, 39)

    def __init__(self, base_sfc, rect, padding=(0, 0, 0, 0), color=_bkg_colour):
        print rect
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


class Button(BaseGui):

    """docstring for Button"""

    def __init__(self, base_sfc, action="", obj="", img=""):
        self.img    = pygame.image.load(img)
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
            print "no action defined"


class Menu(BaseGui):

    def __init__(self, base_sfc, rect, color, buttons, axis):
        super(Menu, self).__init__(base_sfc, rect, color)
        self.initiate_elements(buttons)
        self.fill(color)
        self.populate_sfc(axis)
        self.update_sfc()

    def initiate_elements(self, buttons):
        for button in buttons:
            b = Button(self, button['action'], button[
                       'simulator'], button['img'])
            self.elements.append(b)

    def populate_sfc(self, axis=True, step=20):
        """
        Blits buttons and updates their position

        Keyword arguments:
        axis (boolean) -- Setup menu horizontally or vertically
        steps (integer)  -- Padding to use between buttons

        """
        # axis = True  -> x
        # axis = False -> y
        padding = step
        if axis:
            for button in self.elements:
                button.rect.x = padding
                button.rect.y = step
                padding += button.get_width() + step
        else:
            for button in self.elements:
                button.rect.x = step
                button.rect.y = padding
                padding += button.get_height() + step
        

class Screen(BaseGui):
    """docstring for Screen"""


    def __init__(self, base_sfc, rect, color, elements):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = True
    

    def switchSelect(self):
        self.selected = not self.selected
        if self.selected:
            self.update_sfc()

class InputBox(BaseGui):

    """ Docstring for InputBox"""

    def __init__(self, base_sfc, rect, color):
        super(InputBox, self).__init__(base_sfc, rect, color)
        self.input       = []
        self.inputxt     = ""
        self.inputlst    = []
        self.line_height = 0
        self.line_cont   = 0

    def get_key(self):
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass
    # TODO: refactor variable names/

    def display_box(self, message):
        "Print a message in a box in the middle of the sfc"
        fontobject = pygame.font.Font(None, 18)
        self.line_height = 0
        pygame.draw.rect(self, (0, 0, 0), (0, (
            self.get_height() / 2), self.get_width(), self.get_height() / 2), 0)
        pygame.draw.rect(self, (255, 255, 255), (1, (
            self.get_height() / 2) + 1, self.get_width() - 1, self.get_height() - 1), 1)
        for lines in self.inputlst:
            line = fontobject.render(lines, 1, (255, 255, 255))
            self.blit(line, (0, self.get_height() / 2 + self.line_height))
            self.line_height += line.get_height()
        line = fontobject.render(message, 1, (255, 255, 255))
        self.blit(line, (0, self.get_height() / 2 + self.line_height))
        if line.get_width() > (self.get_width() - 10):
            return True
        else:
            return False

    def get_final_string(self):
        final = ""
        if self.inputlst:
            for i in self.inputlst:
                final += i
        return final

    def convert_to_list(self, full_string):
        try:
            numlist = full_string.rsplit(' ')
            full_list = [int(elem) for elem in numlist]
            return full_list
        except ValueError:
            print "mira si seras gato"
            return None

    def ask(self):

        pygame.font.init()
        current_string = ""
        self.display_box(current_string)
        while True:
            inkey = self.get_key()
            if inkey == K_BACKSPACE:
                if current_string:
                    current_string = current_string[0:-1]
                elif self.inputlst:
                    current_string = self.inputlst.pop()
                self.display_box(current_string)
            elif inkey == K_RETURN:
                self.inputlst.append(current_string)
                break
            elif inkey <= 127:
                current_string += chr(inkey)
                if self.display_box(current_string):
                    self.inputlst.append(current_string)
                    current_string = ""
            self.update_sfc()
        final = self.get_final_string()
        return self.convert_to_list(final)


class Screen(BaseGui):

    """docstring for Screen"""

    def __init__(self, base_sfc, rect, color, elements):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = True

    def switchSelect(self):
        self.selected = not self.selected
        if self.selected:
            self.update_sfc()
