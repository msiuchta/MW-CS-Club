#CS Club Game

import pygame
import random
from array import *

class tile:
    
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
class landTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCords(self):
        return (self.x, self.y)

class oceanTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('ocean.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCords(self):
        return (self.x, self.y)

#Function to Generate Land
def genLand(xx, yy):
    x = xx
    y = yy
    while (x < 49 and x > 1) and (y < 29 and y > 1):
        grid[y][x] = landTile(x*25, y*25, 25, 25)
        grid[y + 1][x] = landTile(x*25, (y+1)*25, 25, 25)
        grid[y - 1][x] = landTile(x*25, (y-1)*25, 25, 25)
        grid[y][x + 1] = landTile((x+1)*25, y*25, 25, 25)
        grid[y][x - 1] = landTile((x-1)*25, y*25, 25, 25)
        #Optional 3X3 Random Walk Generation DO NOT UNCOMMENT
        # grid[y + 1][x + 1] = landTile(x*25, y*25, 25, 25)
        # grid[y + 1][x - 1] = landTile(x*25, y*25, 25, 25)
        # grid[y - 1][x + 1] = landTile(x*25, y*25, 25, 25)
        # grid[y - 1][x - 1] = landTile(x*25, y*25, 25, 25)
        choice = random.randrange(1, 5)
        if choice == 1:
            y -= 1
        elif choice == 2:
            y += 1
        elif choice == 3:
            x -= 1
        else:
            x += 1

def removeIsolatedOcean():
    for row in range(1, 29):
        for col in range(1, 49):  
            if isinstance(grid[row][col], oceanTile):
                surrounded_by_land = (
                    isinstance(grid[row - 1][col], landTile) and
                    isinstance(grid[row + 1][col], landTile) and
                    isinstance(grid[row][col - 1], landTile) and
                    isinstance(grid[row][col + 1], landTile)
                )
                if surrounded_by_land:
                    grid[row][col] = landTile(col * 25, row * 25, 25, 25)

#Total Land Tiles
def checkTotalLand():
    counter = 0
    for row in range(30):
        for col in range(50):
            if isinstance(grid[row][col], landTile):
                counter += 1
    return counter

def isValidGen():
    if (checkTotalLand() > 575 and checkTotalLand() < 700):
        return True
    return False

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

#Gen Land
genLand(random.randrange(0, 50), random.randrange(0, 30))
while not isValidGen(): 
    # genLand(5, 15)
    # genLand(45, 15)

    genLand(10, 5)
    if checkTotalLand() > 700:
        break
    genLand(10, 25)
    if checkTotalLand() > 700:
        break    
    genLand(45, 5)
    if checkTotalLand() > 700:
        break
    genLand(45, 25)
    if checkTotalLand() > 700:
        break
    


    print(checkTotalLand())
removeIsolatedOcean()

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
