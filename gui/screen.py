from base import BaseGui
class Screen(BaseGui):
    """docstring for Screen"""


    def __init__(self, base_sfc, rect, color, elements, last_screen):
        super(Screen, self).__init__(base_sfc, rect, color)
        self.elements = elements
        self.selected = True
        self.last_scr = last_screen
    
    def switchSelect(self):
        self.selected = not self.selected
        if self.selected:
            self.update_sfc()
            # self.last_scr.switchSelect()

    def go_back(self):
        if self.selected:
            self.switchSelect()
        self.last_scr.switchSelect()
