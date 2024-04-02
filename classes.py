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

    def setID(self, x):
        self.ID = x
    
    def returnID(self):
        return self.ID

class oceanTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('ocean.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCords(self):
        return (self.x, self.y)

class territory:
    
    def __init__(self, list):
        self.size = random.randrange(10, 21)
        self.tiles = []
        
        counter = 0
        x = random.randrange(0, 50)
        y = random.randrange(0, 30)

        
        # while (counter < size):
        #     if isInstance(grid[y][x], landTile and checkIfUsedID(grid[y][x].returnID(), usedIDs)==False):
        #         counter += 1
        #         usedIDs.append(grid[y][x].returnID())
