import os
import sys
import pygame
import string
from pygame.locals import *

class BaseGui(pygame.surface.Surface):


    _bkg_colour = (0,0,0)

    def __init__(self, base_sfc, rect, padding=(0, 0, 0, 0), color=_bkg_colour):
        print rect
        super(BaseGui, self).__init__((rect[2], rect[3]))
        self.rect     = self.get_rect()
        self.rect.x   = rect[0]
        self.rect.y   = rect[1]
        self.base_sfc = base_sfc
        self.padding  = padding
        self.elements = []
        self.base_sfc.blit(self, self.rect)   
        pygame.display.update(self.rect)

    def initiate_elements(self):
        pass

    def update_sfc(self):
        if (self.elements):
            for e in self.elements:
                e.update_sfc()
        self.base_sfc.blit(self, (self.rect.x, self.rect.y))
        pygame.display.update(self.base_sfc.get_rect())

class Button(BaseGui):
    """docstring for Button"""


    def __init__(self, base_sfc, action="", simulator="", img=""):
        self.img = pygame.image.load(img)
        self.action = action
        self.simulator = simulator
        super(Button, self).__init__(base_sfc, self.img.get_rect())
    
    def update_sfc(self):
        self.base_sfc.blit(self.img, (self.rect.x, self.rect.y))
    
    def clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def executeAction(self):
        action = getattr(self.simulator, self.action)
        if action:
            return action()
        else:
            print "no action defined"


class Menu(BaseGui):


    def __init__(self, base_sfc, rect, color, buttons, axis):
        super(Menu, self).__init__(base_sfc, rect, color)
        self.initiate_elements(buttons)
        self.populate_sfc(axis)
        self.update_sfc()

    def initiate_elements(self, buttons):
        for button in buttons:
            b = Button(self, button['action'], button['simulator'], button['img'])
            self.elements.append(b)

    def populate_sfc(self, axis=True, step=20):
        # axis = True  -> x
        # axis = False -> y
        padding = step
        if axis:
            for button in self.elements:
                button.rect.x = padding
                button.rect.y = step
                padding += button.get_width()+step
        else:
            for button in self.elements:
                button.rect.x = step
                button.rect.y = padding
                padding += button.get_height()+step
        

class Screen(BaseGui):
    """docstring for Screen"""


    def __init__(self, base_sfc, rect, color, elements):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = True
    
    def showScreen(self):
        self.screen.fill(self.bkg_colour)
        for button in self.buttons:
            self.screen.blit(button.img, button.pos)
        pygame.display.update()

    def switchSelect(self):
        self.screen.fill(self.bkg_colour)
        self.selected = not self.selected



class InputBox(BaseGui):
    """ Docstring for InputBox"""
    def __init__(self, base_sfc, rect, color):
        super(InputBox, self).__init__(base_sfc, rect, color)
        self.input       = []
        self.inputxt     = ""
        self.inputlst    = []
        self.line_height = 0
        self.line_cont   = 0
        self.ask()
        self.update_sfc()

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
                pass
# TODO: refactor variable names/
    def display_box(self, message):
        "Print a message in a box in the middle of the sfc"
        fontobject = pygame.font.Font(None,18)
        self.line_height=0
        # self.fill(self.colour)
        pygame.draw.rect(self, (0,0,0),(0,(self.get_height() / 2),self.get_width(),self.get_height()/2), 0)
        pygame.draw.rect(self, (255,255,255),(1,(self.get_height() / 2) +1,self.get_width()-1, self.get_height()-1), 1)
        if len(message) != 0:
            for lines in self.inputlst:
                line = fontobject.render(lines, 1, (255, 255, 255))
                self.blit(line, (0, self.get_height() / 2 + self.line_height))
                self.line_height += line.get_height()
            line = fontobject.render(message, 1, (255, 255, 255))
            self.blit(line, (0, self.get_height() / 2 + self.line_height))
            # pygame.display.flip()
            if line.get_width() > self.get_width() - 10 :
                self.inputlst.append(message)
                self.line_height =self.line_height + line.get_height()
                return True
            else:
                return False
        

    def ask(self):
        "ask(sfc, question) -> answer"
        pygame.font.init()
        current_string = []
        self.display_box(string.join(current_string,""))
        while 1:
            inkey = self.get_key()
            if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
                if len(self.inputlst) > 0 and current_string == "":
                    self.inputlst.pop()
                    current_string = self.inputlst.pop()
                self.display_box(string.join(current_string,""))
            elif inkey == K_RETURN:
                self.inputlst.append(string.join(current_string,""))
                break
            elif inkey <= 127:
                current_string.append(chr(inkey))
                if self.display_box(string.join(current_string,"")):
                    # self.inputlst.append(string.join(current_string,""))
                    current_string = []
            self.update_sfc()
        print self.inputlst
        # self.inputxt = string.join(current_string,"")
        # return string.join(current_string,"")
