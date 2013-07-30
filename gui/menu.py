from base import BaseGui
class Menu(BaseGui):

    def __init__(self, base_sfc, rect, color, buttons, axis):
        super(Menu, self).__init__(base_sfc, rect, color)
        self.initiate_elements(buttons)
        self.fill(color)
        self.populate_sfc(axis)
        self.update_sfc()

    def initiate_elements(self, buttons):
        for button in buttons:
            b = Button(self, button['action'], button['obj'], button['img'])
            self.elements.append(b)

    def populate_sfc(self, axis=True, step=20):
        """
        Blits buttons and updates their position

        Keyword arguments:
        axis (boolean) -- Setup menu horizontally or vertically
        steps (integer)  -- Padding to use between buttons

        """
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
        