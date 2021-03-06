import sys
import pygame
import time
import config
import queue
import threading
from tkinter import *
from tkinter import ttk
from pygame.locals import *

# Local defined modules
from grid import Grid
from search import Search
from window import *

gridQ = queue.Queue()

config.init()

# Start an instance of tkinter window to get options from user
opt = GridOptions()
opt.mainloop()

# Record options selected by user
Grid_size = opt.shared_data["Grid_size"].get()
Start_row = opt.shared_data["Start_row"].get()
s_c = opt.shared_data["Start_column"].get()
g_r = opt.shared_data["Goal_Row"].get()
g_c = opt.shared_data["Goal_column"].get()
Search_Algorithm = opt.shared_data["Search_Algorithm"].get()

row = (0, 0)
col = (0, 0)

# NOTE: Grid size is square at this point. Implementing with row/col values so I have the option
# to make grid rectangular or more user-defined later on
if Grid_size == "Small":
    row = (200, 10)
    col = (200, 10)
elif Grid_size == "Medium":
    row = (500, 25)
    col = (500, 25)
elif Grid_size == "Large":
    row = (800, 40)
    col = (800, 40)

# Main instances of search grid (Grid) and search Search_Algorithms(Search)
myGrid = Grid(row[0], col[0])
myMatrix = Search(gridQ, row[1], col[1], (Start_row, s_c), (g_r, g_c))


# Start the visualisation and initialize the grid
pygame.init()
myGrid.initGrid()

# Add the starting and goal states to the grid
myGrid.fillSquare(Start_row, s_c, config.yellow)
myGrid.fillSquare(g_r, g_c, config.yellow)

# Local vars for recording mouse input from pygame
pos_x = 0
pos_y = 0
getWalls = True
fillCells = False

# While spacebar hasn't been pressed, record mouse clicks to record walls input by user
while getWalls:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_SPACE:
                getWalls = False
        elif event.type == MOUSEBUTTONDOWN:
            fillCells = True
        elif event.type == MOUSEBUTTONUP:
            fillCells = False

        # Check if user has selected any walls to add to the grid
        if fillCells:
            try:
                # Get event pos and then convert coordinates to an actual location on the grid
                # Color in the cell and set the coordinates in matrix to non-visitable
                pos_x, pos_y = event.pos
                pos_x, pos_y = myGrid.getCell(pos_x, pos_y)
                rec = pygame.Rect(pos_x, pos_y, 20, 20)
                pygame.draw.rect(myGrid.screen, config.fill, rec)
                myMatrix.setCell(pos_y // 20, pos_x // 20, "B")
                pygame.display.update()
            except:
                pass
    pygame.display.flip()

# Start a thread of the Search_Algorithm user selected
if Search_Algorithm == "BFS":
    t1 = threading.Thread(target=myMatrix.bfs())
elif Search_Algorithm == "DFS":
    t1 = threading.Thread(target=myMatrix.dfs())
elif Search_Algorithm == "A-Star":
    t1 = threading.Thread(target=myMatrix.a_star())

t1.start()

# Color in cells from the search Search_Algorithm and wait for quitgame
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if not gridQ.empty():
        x, y, clr = gridQ.get()

        myGrid.fillSquare(x, y, clr)
        pygame.display.update()


# main()
