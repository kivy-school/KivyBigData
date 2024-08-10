import matplotlib.pyplot as plt
import numpy as np

# Create data
from random import randint

class Cell:
    def __init__(self, cell_num, value):
        self.cell_num = cell_num
        self.value = value

class SamplerBox:
    def __init__(self, box_num):
        self.box_num = box_num
        self.cells = []
        for i in range(1, 13):
            self.cells.append(Cell(i + ((box_num - 1) * 12), randint(0, 200) / 100.0))

# Populate a list with 20 boxes
all_boxes = []
for i in range(1, 21):
    all_boxes.append(SamplerBox(i))

# Prepare data for the 2D histogram
x_values = [cell.cell_num for box in all_boxes for cell in box.cells]
y_values = [cell.value for box in all_boxes for cell in box.cells]

# Create 2D histogram
plt.figure(figsize=(10, 6))
plt.hist2d(x_values, y_values, bins=[24, 20], cmap='plasma')  # Adjust bins as needed

# Add color bar
plt.colorbar(label='Frequency')

# Labels and title
plt.title("2D Histogram of Sampler Values Across Cells")
plt.xlabel("Cell Number")
plt.ylabel("Sampler Value")

plt.show()
