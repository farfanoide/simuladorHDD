from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# Builder.load_file('my.kv')

class LoginScreen(GridLayout):

	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 4
		self.rows = 4
		self.add_widget(Label(text='Posicion Inicial'))
		self.init_pos = TextInput(multiline=False)
		self.add_widget(self.init_pos)
		self.add_widget(Label(text='Direccion inicial'))
		self.direction = TextInput(multiline=False)
		self.add_widget(self.direction)

class MyApp(App):

	def build(self):
		return LoginScreen(cols=2)


if __name__ == '__main__':
	MyApp().run()