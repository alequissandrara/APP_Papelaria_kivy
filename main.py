from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

Builder. load_file('tela.kv')

class MyLayout(Widget):
    pass
class TelaPet(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()
TelaPet().run()