from kivy.uix.label import Label
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.uix.relativelayout import RelativeLayout


class Graphic(RelativeLayout):

    """Graphic class to print requirements to canvas"""
    def __init__(self, **kargs):
        super(Graphic, self).__init__(**kargs)
        self.reqs = []
        self.dir = None
        self.method = None
        self.movs = 0

    def _calculate_vertical_step(self, requirements):
        """Calculates distance between each requirement based on height available and amount of requirements."""

        reqs_quantity = 0

        for reqs in requirements:
            print reqs
            if reqs:
                reqs_quantity += len(reqs)

        step = int(self.height / reqs_quantity)
        return step

    def _calculate_coordinates(self, requirements):
        """Calculates coordinates for the graphic according to amount of requirements and height available."""

        step = self._calculate_vertical_step(requirements)
        coordinates = ([], [], [])
        points = []
        coor_y = self.height
        for x in range(len(requirements)):
            try:
                for req in requirements[x]:
                    coordinates[x].append(req)
                    coordinates[x].append(coor_y)
                    points.append((req, coor_y))
                    coor_y -= step
            except IndexError:
                pass
        # update page faults line with first req of next line
        if (coordinates[0]) and (coordinates[1]):
            coordinates[0].extend(coordinates[1][:2])
            
        return coordinates, points

    def draw_lines(self, requirements):
        self.draw_grid()
        coordinates, points = self._calculate_coordinates(requirements)
        with self.canvas:
            for x in range(len(coordinates)):
                if coordinates[x]:
                    Color(0, 1, 0) if x else Color(1, 0, 0)
                    Line(points=coordinates[x], width=1)
        
        ps = 5. # circle diameter
        for point in points:
            if point[0] < self.width - 20:
                self.add_widget(Label(text=str(int(point[0])), pos=(point[0], point[1]-20), size_hint=(.1,.1)))
            else:
                self.add_widget(Label(text=str(int(point[0])), pos=(point[0]-45, point[1]-20), size_hint=(.1,.1)))
            with self.canvas:    
                Color(0, 0, 1)
                Ellipse(size=(ps, ps), pos=(point[0] - (ps / 2), point[1] - (ps / 2)))

    def draw_grid(self):

        self.canvas.clear()
        # self.clear_widgets()

        with self.canvas:
            Line(rectangle=(0, 0, self.width, self.height))

        step = self.width / 10
        print step
        # step = 50
        for x in xrange(0, self.width, step):
            self.add_widget(
                Label(text=str(x), pos=(x - step / 2, self.height), size_hint=(.1, .1)))
            with self.canvas:
                Line(points=[x, 0, x, self.height], width=1)

        