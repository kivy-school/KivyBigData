from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty

class MyGrid(GridLayout):
    data = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2  # Adjust columns as needed
        self.bind(data=self.update_buttons)
        self.create_buttons()

    def create_buttons(self):
        for item in self.data:
            button = Button(text=str(item))
            self.add_widget(button)

    def update_buttons(self, instance, value):
        for i, button in enumerate(self.children):
            if i < len(value):
                button.text = str(value[i])

class MyApp(App):
    def build(self):
        grid = MyGrid()
        grid.data = [1, 2, 3, 4]  # Initial data
        return grid

if __name__ == '__main__':
    MyApp().run()
