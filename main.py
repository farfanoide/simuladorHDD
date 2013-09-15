import sys
import os
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.settings import Settings, SettingsPanel
from kivy.config import Config, ConfigParser
# -----------------
from simulator import Simulator
from graphic import Graphic

# -----------
# TODO: get these their own place
# -----------
# HELPERS
# -----------


def str_to_list(string):
    str_list = string.rsplit(' ')
    num_list = []
    for elem in str_list:
        elem.strip(' ')
        try:
            elem = int(elem)
        except ValueError:
            pass
        else:
            num_list.append(elem)
    return num_list


def load_file(name):
    """ Load data from a file"""
    try:
        f = open(name, 'r')
        lines = f.readlines()
        full_list = str_to_list(lines[0])
        return full_list
    except IOError:
        return None


class PymulatorApp(App):
    # TODO: start tagging the app.

    use_kivy_settings = False

    def build_config(self, config):
        # TODO: add validations for missing or incomplete .ini
        config.read('pymulator.ini')

    def build_settings(self, settings):
        settings.add_json_panel('Pymulator', self.config, 'settings.json')

    def build(self):
        self.simulator = Simulator()
        self.simulator.direction = int(
            self.config.getdefault('pymulator', 'dir', True))
        self.simulator.init_pos = int(
            self.config.getdefault('pymulator', 'init_pos', 250))
        self.simulator.random_list(
            int(self.config.getdefault('pymulator', 'reqs', 15)))
        self.simulator.add_random_pf(
            int(self.config.getdefault('pymulator', 'pf', 3)))

    def on_config_change(self, config, section, key, value):
        # TODO: change self.simulator.x to use kivy properties
        # set max, min and validations
        #  also create custom function for every key with validations and stuff
        if config is not self.config:
            return
        if key == 'dir':
            self.simulator.direction = value
        elif (key == 'reqs'):
            self.simulator.random_list(int(value))
            self.simulator.add_random_pf(
                int(self.config.getdefault('pymulator', 'pf', 3)))
        elif key == 'init_pos':
            self.simulator.init_pos = int(value)
        elif key == 'pf':
            self.simulator.random_list(
                int(self.config.getdefault('pymulator', 'reqs', 15)))
            self.simulator.add_random_pf(int(value))
        elif key == 'file':
            reqs = load_file(value)
            if reqs:
                self.simulator.set_requirements(reqs)
            else:
                # TODO: move popup to self containing function
                # that receives title of section and message
                popup = Popup(title='Lista de Requerimientos',
                              content=Label(
                                  text='El archivo ingresado no pudo ser leido \n o no esta en el formato correcto'),
                              size_hint=(None, None), size=(600, 300))
                popup.open()
                self.config.set('pymulator', 'file', None)
        elif key == 'req_list':
            reqs = str_to_list(value)
            if reqs:
                self.simulator.set_requirements(reqs)


if __name__ == '__main__':
    PymulatorApp().run()
