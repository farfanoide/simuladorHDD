from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
# from kivy.vector import Vector
from kivy.clock import Clock
from simulator import Simulator
from kivy.config import Config

simulator = Simulator()
simulator.requirements = [-5, 15, 40, 65, 20, -35, -400, 90, 100]

# class GraphicsScreen(Screen):
#     pass

# class GraphicWidget(Widget):
#     pass

# class MainScreen(Screen):
#     pass

class PymulatorApp(App):
	Config.set('graphics','resizable','0')
	pass
    # def build(self):
        # self.root = ScreenManager()
        # self.root.add_widget(GraphicsScreen(name='graphics'))
        # self.root.add_widget(MainScreen(name='main'))




if __name__ == '__main__':
    PymulatorApp().run()
