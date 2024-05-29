import random
from classes import *

#Random Walk Land Generation
def genLand(xx, yy, grid):
    x = xx
    y = yy
    while (x < 49 and x > 1) and (y < 29 and y > 1):
        grid[y][x] = landTile(x*25, y*25, 25, 25)
        grid[y + 1][x] = landTile(x*25, (y+1)*25, 25, 25)
        grid[y - 1][x] = landTile(x*25, (y-1)*25, 25, 25)
        grid[y][x + 1] = landTile((x+1)*25, y*25, 25, 25)
        grid[y][x - 1] = landTile((x-1)*25, y*25, 25, 25)
        choice = random.randrange(1, 5)
        if choice == 1:
            y -= 1
        elif choice == 2:
            y += 1
        elif choice == 3:
            x -= 1
        else:
            x += 1

#Removes Ocean Tiles Surrounded By Land
def removeIsolatedOcean(grid):
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

#Returns Total Land Tiles
def checkTotalLand(grid):
    counter = 0
    for row in range(30):
        for col in range(50):
            if isinstance(grid[row][col], landTile):
                counter += 1
    return counter

#Checks if there is a "perfect" amount of land tiles
def isValidGen(grid):
    if (checkTotalLand(grid) > 575 and checkTotalLand(grid) < 700):
        return True
    return False

#Work In Progess, Checks If Tile Controlled By Another Player
def checkIfUsedID(id, ids):
    for a in range(0, ids.size()):
        if id == ids[a]:
            return True
    return False
    
#def selectTile(grid, x, y):
    #for event.pos

#karu beta and legoatie suffered while making this
#Gives Proper Coastal Texture To All Land Tiles
def fixTextures(grid):
    for row in range(29):
        for col in range(49):
            if isinstance(grid[row][col], landTile):
                if  (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col - 1], oceanTile) and isinstance(grid[row][col + 1], landTile)):                
                    img = pygame.image.load('CoastL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastT.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastB.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastTR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastBL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastBR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastTL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3B.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3T.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3L.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('Coast3R.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastPH.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastPV.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], oceanTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDBL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], oceanTile)):
                    img = pygame.image.load('CoastDBR.png')
                    grid[row][col].setTexture(img)             
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], oceanTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDTL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], oceanTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDTR.png')
                    grid[row][col].setTexture(img)