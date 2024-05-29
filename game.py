#CS Club Game

import pygame
import random
from array import *
from classes import *
from functions import *

#Player and Territory Management
usedIDs = []
players = []

#Setting up Initial Player Screen
pygame.init()
Background_color = (48, 55, 191)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 850
screen0 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen0.fill(Background_color)
rect2 = pygame.Rect(200, 200, 100, 100)
rect3 = pygame.Rect(625, 200, 100, 100)
rect4 = pygame.Rect(1050, 200, 100, 100)
rect5 = pygame.Rect(412, 650, 100, 100)
rect6 = pygame.Rect(838, 650, 100, 100)
pygame.draw.rect(screen0,(153, 32, 28),rect2)
pygame.draw.rect(screen0,(153, 32, 28),rect3)
pygame.draw.rect(screen0,(153, 32, 28),rect4)
pygame.draw.rect(screen0,(153, 32, 28),rect5)
pygame.draw.rect(screen0,(153, 32, 28),rect6)
pygame.display.flip()
running0 = True 
while running0:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            numplayer = 0
            if rect2.collidepoint(event.pos):
                numplayer = 2
                #pygame.screen0.quit()
                running0 = False
            if rect3.collidepoint(event.pos):
                numplayer = 3
                #pygame.screen0.quit()
                running0 = False
            if rect4.collidepoint(event.pos):
                numplayer = 4
                #pygame.screen0.quit()
                running0 = False
            if rect5.collidepoint(event.pos):
                numplayer = 5
                #pygame.screen0.quit()
                running0 = False
            if rect6.collidepoint(event.pos):
                numplayer = 6
                #pygame.screen0.quit()
                running0 = False
    pygame.display.update()

# for a in range (numplayers):
#     players[a] = player(placeholdername, placeholdercolor)

#Setting up Game Screen & Tiles
Background_color = (50, 168, 82)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 850
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
x = 0
count = 0
for col in range(50):
    grid[0][count] = oceanTile(x, 0, 25, 25)
    x += 25
    count += 1
x = 0
count = 0
for col in range(50):
    grid[29][count] = oceanTile(x, 725, 25, 25)
    x += 25
    count += 1
y = 0
count = 0
for row in range(30):
    grid[count][0] = oceanTile(0, y, 25, 25)
    count += 1
    y += 25
y = 0
count = 0
for row in range(30):
    grid[count][49] = oceanTile(1225, y, 25, 25)
    count += 1
    y += 25
removeIsolatedOcean(grid)
print(checkTotalLand(grid))
fixTextures(grid)

#Giving all Land Tiles an ID
counter = 0
for row in range(30):
    for col in range(50):
            counter += 1
            grid[row][col].setID(counter)

#Game Loop
running = True
while running:

    # Hovering Mouse
    mouse_pos = pygame.mouse.get_pos()  
    my = mouse_pos[1] // 25
    mx = mouse_pos[0] // 25
    if my < 30:
        tilex = grid[my][mx].getCordsx() 
    if my < 30:
        tiley = grid[my][mx].getCordsy()
    wowzer=pygame.image.load('white.png')
  
    # All user inputs work through this
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          x= event.pos 

    #Expand Option
    mouse_pos = pygame.mouse.get_pos()  
    tilechecky = mouse_pos[1] // 25
    tilecheckx = mouse_pos[0] // 25                   
    
    #Recreating Screen
    screen1.fill(Background_color)
    for row in range(30):
        for col in range(50):
            grid[row][col].draw(screen1)
            if tiley < 749:
                screen1.blit(wowzer, (tilex, tiley))
                
    pygame.display.update()
