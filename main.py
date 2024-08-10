from kivy.utils import platform

#avoid conflict between mouse provider and touch (very important with touch device)
#no need for android platform
if platform != 'android':
    from kivy.config import Config
    Config.set('input', 'mouse', 'mouse,disable_on_activity')

from kivy.lang import Builder
# from kivy.app import App
from graph_generator import GraphGenerator
import kivy_matplotlib_widget  #register all widgets to kivy register
from kivy.properties import ListProperty

import trio
from kivy.lang import Builder

from kivy_reloader.app import App

KV = '''

Screen
    figure_wgt:figure_wgt
    BoxLayout:
        orientation:'vertical'
        MatplotFigure:
            id: figure_wgt
            size_hint: (1, 0.3)
        # BoxLayout:
        #     id: homeBL
        #     size_hint_y:0.2
        #     Button:
        #         text:"home"
        #         on_release:app.home()
        #     ToggleButton:
        #         group:'touch_mode'
        #         state:'down'
        #         text:"pan" 
        #         on_release:
        #             app.set_touch_mode('pan')
        #             self.state='down'
        #     ToggleButton:
        #         group:'touch_mode'
        #         text:"zoom box"  
        #         on_release:
        #             app.set_touch_mode('zoombox')
        #             self.state='down'                
        BoxLayout:
            size_hint: (1, 0.1)
            id: topBL
            orientation: 'horizontal'
            GridLayout: 
                id: top_datagrid
                cols: 20
                spacing: 1
                padding: 1
        BoxLayout:
            id: bottomBL
            orientation: 'horizontal'
            GridLayout: 
                id: bot_datagrid
                cols: 20
                spacing: 1
                padding: 1
'''

from kivy.clock import Clock
import numpy as np

from kivy.uix.button import Button

from random import randint


class Cell:
    # Each cell has a number and a sampler value
    def __init__(self, cell_num, value):
        self.cell_num = cell_num
        self.value = value


class SamplerBox:
    # Each box measures 12 samplers
    def __init__(self, box_num):
        self.box_num = box_num
        self.cells = []
        self.sampler_update()

    def sampler_update(self):
        for i in range(1, 13):
            # Some fake random data
            self.cells.append( Cell(i + ((self.box_num -1)*12), randint(0, 200)/100.0))

all_boxes = []

def Sample_set():
    Ans= []
    for i in range(1,21):
        Ans.append(SamplerBox(i))
    return Ans

all_boxes = Sample_set()
print("ss type", type(all_boxes))
print("ss type2", all_boxes)
print("ss type3", len(all_boxes))
print("PRINT ONLY CELLS IN 1st SamplerBox", )
b1 = all_boxes[0]
for cell in b1.cells:
        print(f'{b1.box_num}\t\t{cell.cell_num}\t\t{cell.value}')
breakpoint()

class Test(App):
    current_boxes = ListProperty() #updating this property forces changes 

    def build(self):  
        self.title = 'Kivy Data'
        self.screen=Builder.load_string(KV)
        return self.screen

    def on_start(self, *args):
        self.mygraph = GraphGenerator()
        print("ggg", type(self.mygraph), self.mygraph)
        
        self.screen.figure_wgt.figure = self.mygraph.fig
        #update the graph with a shitty graphgen
        Clock.schedule_interval(self.updateGraph, 1)
        for i in range(20,0,-1): # should be cols
            button = Button(text=f'B{i}', font_size="10")
            datagridref = app.get_running_app().root.ids['top_datagrid']
            datagridref.add_widget(button)
        for i in range(240): # should be rows*cols
            # button = Button(text=f'{i + 1}')
            button = Button(text=f'{i + 1} \n{i+1}', font_size="10")
            datagridref = app.get_running_app().root.ids['bot_datagrid']
            datagridref.add_widget(button)

    def updateGraph(self, *args):
        nb_pts=50000

        #clear old plots
        self.mygraph.ax1.clear()

        #tell graph to redraw somehow

        self.mygraph.line1 = self.mygraph.ax1.plot(np.random.randn(nb_pts),label='line1')
        self.mygraph.line2 = self.mygraph.ax1.plot(np.random.randn(nb_pts)+2,label='line2') 
        # app.get_running_app().root.ids['figure_wgt'].update()
        #make it enabled so it updates
        # app.get_running_app().root.ids['figure_wgt'].diabled = False 
        # app.get_running_app().root.ids['figure_wgt'].background = None
        # app.get_running_app().root.ids['figure_wgt']._pressed = True
        app.get_running_app().root.ids['figure_wgt'].home()
        # app.get_running_app().root.ids['figure_wgt'].axes.figure.canvas.draw_idle()
        # app.get_running_app().root.ids['figure_wgt'].axes.figure.canvas.flush_events()
        # app.get_running_app().root.ids['figure_wgt']._update_view()
        # app.get_running_app().root.ids['figure_wgt']._pressed = False
        print("updated graph")
        self.newset = Sample_set()

        # for box in self.newset:
        #     for cell in box.cells:
        #         print(f'{box.box_num}\t\t{cell.cell_num}\t\t{cell.value}')

        for boxInt, cellInt in itertools.product(range(len(all_boxes)), range(len(all_boxes[0].cells))):
            # print(f'{all_boxes[boxInt].box_num}\t\t{all_boxes[boxInt][cellInt].cell_num}\t\t{all_boxes[boxInt][cellInt].value}')
            print(f'{all_boxes[boxInt].box_num}\t\t{all_boxes[boxInt].cells[cellInt].cell_num}\t\t{all_boxes[boxInt].cells[cellInt].value}')

        

        print("updated bot BL")
        

    def set_touch_mode(self,mode):
        self.screen.figure_wgt.touch_mode=mode

    def home(self):
        self.screen.figure_wgt.home()
        
# app = Test()
# trio.run(app.async_run, "trio")