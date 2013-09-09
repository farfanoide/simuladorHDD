from kivy.app import  App
from kivy.uix.label import Label

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import NumericProperty, ReferenceListProperty,\
   ObjectProperty
# from kivy.vector import Vector
from kivy.clock import Clock
	
class SettingsScreen(Screen):
   pass

class MenuScreen(Screen):
   pass

class GraficoScreen(Screen):
  pass  

class PymulatorApp(App):

   def build(self):
#        self.transition = SlideTransition(duration=.35)
       self.root = ScreenManager()
       settings = SettingsScreen(name="settings screen")
       self.root.add_widget(settings);
       menu = MenuScreen(name="Menu Screen")
       self.root.add_widget(menu)
       grafico = GraficoScreen(name="Grafico Screen")
       self.root.add_widget(grafico)

class GraphicArea(Widget):
	pass


if __name__ == '__main__':
   PymulatorApp().run()