# template_app/main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)

        self.add_widget(Label(text="My First Kivy App", font_size=28))

        self.entry = TextInput(hint_text="Type something...", multiline=False)
        self.add_widget(self.entry)

        btn = Button(text="Say Hello", size_hint=(1, 0.3))
        btn.bind(on_press=self.say_hello)
        self.add_widget(btn)

        self.output = Label(text="", font_size=22)
        self.add_widget(self.output)

    def say_hello(self, instance):
        name = self.entry.text.strip() or "World"
        self.output.text = f"Hello, {name}!"


class MyApp(App):
    def build(self):
        self.title = "My Kivy App"
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()