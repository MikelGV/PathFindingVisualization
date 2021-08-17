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
            pygame.draw.rect(screen, color, (self.col * w, self.row * h, w, h), st)
            pygame.display.update()


cols = 50
grid = [0 for col in range(cols)]
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

for col in range(cols): # Create 2d array
    grid[col] = [0 for col in range(row)]

for col in range(cols): # Create Spots
    for row in range(rows):
        grid[col][row] = Spot(col, row)

# Start and end node
start = grid[12][5]
end = grid[3][6]

for col in range(cols): # Show rect
    for row in range(rows):
        grid[col][row].show((255, 255, 255), 1)