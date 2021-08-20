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

showPath.grid(columnspan=2, row=2)
submit.grid(columnspan=2, row=3)
label1.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)

window.update()
mainloop()

pygame.init()
open_set.append(start)

def mouse_press(x):
    t = x[0]
    w = x[1]
    g1 = t // (800 // cols)
    g2 = w // (800 // rows)
    acess = grid[g1][g2]
    if (acess != start) and (acess != end):
        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)

end.show((255, 8, 127), 0)
start.show((255, 8, 127), 0)

loop = True

while loop:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            mouse_press(pos)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

def heuristic(n , e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    return d


def main():
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    if len(open_set) > 0:
        lowest_index = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[lowest_index].f:
                lowest_index = -1
        current = open_set[lowest_index]
        if current == end:
            print('done', current.f)
            start.show((255, 8, 127), 0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.show((0, 0, 255), 0)
                current = current.previous
            end.show((255, 8, 127), 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Program Finished', ('The program finished, the shortest distance \n to the path is ' + str(temp) + 'blocks away, \n would you like to re run the program?'))
            if result == True:
                os.execl(sys.executable, sys.executable, sys.argv)
            else:
                ag = True
                while ag:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            ag = False
                            break
            pygame.quit()
        open_set.pop(lowest_index)
        close_set.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in close_set:
                tempG = current.g + current.value
                if neighbor in open_set:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    open_set.append(neighbor)
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(open_set)):
            open_set[i].show(green, 0)
        
        for i in range(len(close_set)):
            if close_set[i] != start:
                close_set[i].show(red, 0)
    current.closed = True

while True:
    events = pygame.event.poll()
    if events.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()

