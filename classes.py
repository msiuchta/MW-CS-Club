import pygame
import random
from array import *

class rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('white.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    

class tile:
    
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.ID = 0
        self.width = width
        self.height = height
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def setID(self, x):
        self.ID = x
        
    def getID(self):
        return self.ID

    def getRow(self, id):
        row = (id - 1) // 50
        return row
    
    def getCol(self, id):
        col = (id - 1) % 50
        return col
    
class landTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCordsx(self):
        return (self.x)

    def getCordsy(self):
        return (self.y)
    
    def returnID(self):
        return self.ID
    
    def setTexture(self, texture):
        self.image = texture

class oceanTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('ocean.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCordsx(self):
        return (self.x)
    
    def getCordsy(self):
      return (self.y)


class player:
    def __init__(self, name, color):
        self.territories = []
        self.name = name
        self.color = color
        
        #Game mechanics related variables
        self.population = 0
        self.army = 0
        self.gold = 0
        self.wood = 0
        self.stone = 0
        self.food = 0

    def addTerritoryToPlayer(self, id):
        self.territories.append(id)

    def doesTileBelongToPlayer(self, id):
        for a in range(0, self.territories.size()):
            if id == self.territories[a]:
                return True
        return False

    def checkExpandable(self, id, grid):
        if (self.doesTileBelongToPlayer(grid[(self.getRow(id))-1][self.getCol(id)].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[(self.getRow(id))+1][self.getCol(id)].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[self.getRow(id)][(self.getCol(id))-1].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[self.getRow(id)][(self.getCol(id))+1].getID())):
            return True
        return False        

        
        
    
      
            
      

        
   
