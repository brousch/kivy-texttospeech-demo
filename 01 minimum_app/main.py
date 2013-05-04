import kivy
kivy.require('1.6.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TtsDemo(BoxLayout):
    pass

class TtsDemoApp(App):
    def build(self):
        return TtsDemo()
    

if __name__ == '__main__':
    TtsDemoApp().run()
