


import pygame
from .mouseClick import MouseClick

class Button():
  def __init__(self, 
               x=0, y=0, width=100, height=30, color=(0,0,0)):
    
    # Basic variables
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    # Colors
    self.color = color

    # Mouse click/hover logic
    self.mouseLogic = MouseClick()
    self.cursor = "hand"


  def run(self, screen, mouse):

    # The package with information that is to be returned to the main loop if needed
    returnPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":None, "id":None, "type":None }

    # Check for hover and click
    self.mouseLogic.run((self.x, self.y), (self.width, self.height), mouse)

    if self.mouseLogic.hoverTest == True:
      returnPackage["changeCursor"] = True

    if self.mouseLogic.hoverTest == True:
      pygame.draw.rect(screen, (100,0,100), (self.x, self.y, self.width, self.height))
    else:
      pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    return returnPackage


