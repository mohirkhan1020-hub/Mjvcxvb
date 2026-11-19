from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='Hello Python Kivy APK!')

if __name__ == '__main__':
    MainApp().run()