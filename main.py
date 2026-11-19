from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=30, spacing=20, **kwargs)

        # Title
        self.add_widget(Label(text="My Kivy App", font_size=32, color=(1, 1, 1, 1)))

        # Input
        self.entry = TextInput(hint_text="Type your name...", multiline=False, size_hint=(1, 0.2))
        self.add_widget(self.entry)

        # Button
        btn = Button(text="Say Hello", size_hint=(1, 0.2), background_color=(0.5, 0.2, 0.8, 1))
        btn.bind(on_press=self.say_hello)
        self.add_widget(btn)

        # Output
        self.output = Label(text="", font_size=24, color=(0, 1, 0, 1))
        self.add_widget(self.output)

    def say_hello(self, instance):
        name = self.entry.text.strip() or "World"
        self.output.text = f"Hello, {name}!"

class MyApp(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    MyApp().run()


