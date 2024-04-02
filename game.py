#CS Club Game

import pygame
import random
from array import *
from classes import *
from functions import *

#Setting up Screen & Tiles
pygame.init()
Background_color = (50, 168, 82)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 750
screen1 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen1.fill(Background_color)
grid = []
for row in range(30):
    temp_row = []
    for col in range(50):
        x = col * 25
        y = row * 25
        temp_row.append(oceanTile(x, y, 25, 25))
    grid.append(temp_row)

#Generate Map
genLand(random.randrange(0, 50), random.randrange(0, 30), grid)
while not isValidGen(grid): 
    genLand(10, 5, grid)
    if checkTotalLand(grid) > 700:
        break
    genLand(10, 25, grid)
    if checkTotalLand(grid) > 700:
        break    
    genLand(45, 5, grid)
    if checkTotalLand(grid) > 700:
        break
    genLand(45, 25, grid)
    if checkTotalLand(grid) > 700:
        break
    print(checkTotalLand(grid))
removeIsolatedOcean(grid)
print(checkTotalLand(grid))

#Giving all Land Tiles an ID
counter = 0
for row in range(30):
    for col in range(50):
        if isinstance(grid[row][col], landTile):
            counter += 1
            grid[row][col].setID(counter)

usedIDs = []




#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Recreating Screen
    screen1.fill(Background_color)
    for row in range(30):
        for col in range(50):
            grid[row][col].draw(screen1)
        
    
    pygame.display.update()
