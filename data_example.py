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


# Populate a list of with 20 boxes
all_boxes = []
for i in range(1,21):
    all_boxes.append(SamplerBox(i))

# Prints examples
print("Box\t\tCell\t\tVal")
# for box in all_boxes:
#     for cell in box.cells:
#         print(f'{box.box_num}\t\t{cell.cell_num}\t\t{cell.value}')
for box in all_boxes:
    for cell in box.cells:
        print(f'{box.box_num}\t\t{cell.cell_num}\t\t{cell.value}')
print("=-=-=-==-=-=-=ZIP VER=-=-=-==-=-=-==-=-=-=")

# for boxInt, cellInt in zip(range(len(all_boxes)), range(len(all_boxes[0].cells))):
import itertools
for boxInt, cellInt in itertools.product(range(len(all_boxes)), range(len(all_boxes[0].cells))):
    print(f'{all_boxes[boxInt].box_num}\t\t{all_boxes[boxInt].cells[cellInt].cell_num}\t\t{all_boxes[boxInt].cells[cellInt].value}')


print("=-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=")
sbox = all_boxes[0]
print(sbox)
print(sbox.box_num)
print(sbox.cells)
scell = sbox.cells[0]
print(scell.cell_num)
print(scell.value)

import trio
from kivy.lang import Builder

from kivy_reloader.app import App

kv = """
Button:
    text: "Hello World"
"""


class MainApp(App):
    def build(self):
        self.title = 'kivydata'
        return Builder.load_string(kv)


app = MainApp()
trio.run(app.async_run, "trio")