from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.clock import Clock

from random import random

kv = """
<DataBox>:  # a BoxLayout with ButtonBehavior
    orientation: 'vertical'
    canvas:
        Color:  
            rgb: .6, .6, .6
        Line:
            rectangle: (*self.pos, *self.size)
        Color:
            rgba: (0, .5, 0, .25) if self.value >= 1 else (.5, 0, 0, .5)
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: f'{root.value:1.2f}'
    Label:
        text: f'{root.index}'
        font_size: sp(10)

<EditPopup>:
    size_hint: .7, .7
    BoxLayout: 
        orientation: 'vertical'
        Label:
            text: 'Edit Controls here'
        BoxLayout:
            size_hint_y: None
            height: dp(48)
            Button:
                text: 'Cancel'
                on_release: root.dismiss()
            Button:
                text: 'OK'
                on_release: root.dismiss()

BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Update Test'
        size_hint_y: None
        height: dp(30)
    DataGrid:
        rows: 12
        cols: 20
"""

class EditPopup(Popup):
    pass

class DataBox(ButtonBehavior, BoxLayout):
    index = NumericProperty()
    value = NumericProperty(1)

    def on_release(self):
        EditPopup(title=f'Edit Control for index: {self.index}').open()


class DataGrid(GridLayout):
    def on_kv_post(self, base_widget):
        for i in range(1, self.rows * self.cols + 1):
            self.add_widget(DataBox(index=i))
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        for w in self.children:
            w.value = random() * 10


class TestGridUpdate(App):
    def build(self):
        return Builder.load_string(kv)


TestGridUpdate().run()