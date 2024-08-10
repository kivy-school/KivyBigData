from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridApp(App):
    def build(self):
        # Create a GridLayout with 3 columns and an unspecified number of rows
        grid_layout = GridLayout(cols=3, spacing=10, padding=10)

        # Create and add buttons to the GridLayout
        for i in range(9):  # 9 buttons (3x3 grid)
            button = Button(text=f'Button {i + 1}')
            grid_layout.add_widget(button)

        return grid_layout

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.always_on_top = True
    MyGridApp().run()
