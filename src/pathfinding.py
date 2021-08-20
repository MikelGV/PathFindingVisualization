import pygame
import math
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

screen = pygame.display.set_mode((800, 800))

class Spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1
    
    def show(self, color, st):
        if self.closed == False:
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()
    
    def path(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

    def add_neighbors(self, grid):
        i = self.i
        j = self.j

        if i < cols -1 and grid[self.i + 1][j].obs == False:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].obs == False:
            self.neighbors.append(grid[self.i - 1][j])
        if i < rows -1 and grid[self.i][j + 1].obs == False:
            self.neighbors.append(grid[self.i][j + 1])
        if i > 0 and grid[self.i][j - 1].obs == False:
            self.neighbors.append(grid[self.i][j - 1])
        
        
        


cols = 50
grid = [0 for i in range(cols)]
rows = 50
open_set = []
close_set = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 800 / cols
h = 800 / rows
came_from = []

for i in range(cols): # Create 2d array
    grid[i] = [0 for i in range(rows)]

for i in range(cols): # Create Spots
    for j in range(rows):
        grid[i][j] = Spot(i, j)

# Start and end node
start = grid[12][5]
end = grid[3][6]

for i in range(cols): # Show rect
    for j in range(rows):
        grid[i][j].show((255, 255, 255), 1)

for i in range(0,rows):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols - 1][i].obs = True
    grid[cols - 1][i].show(grey, 0)
    grid[i][rows - 1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][0].obs = True

def on_submit():
    global start
    global end
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()

window = Tk()
label = Label(window, text="Start(x,y):" )
startBox = Entry(window)
label1 = Label(window, text="End(x,y): ")
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text="Show Steps: ", onvalue=1, offvalue=0, variable=var)

submit = Button(window, text="Submit", command=on_submit)

showPath.grid(columnspan=2, rows=2)
submit.grid(columnspan=2, rows=3)
label1.grid(rows=1, pady=3)
endBox.grid(rows=1, column=1, pady=3)
startBox.grid(rows=0, column=1, pady=3)
label.grid(rows=0, pady=3)

window.update()
mainloop()

pygame.init()
open_set.append(start)


