import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

#kivy program
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()