


import pygame
from .mouseClick import MouseClick

class Button():
  def __init__(self, 
               x=0, y=0, width=100, height=30,

               backgroundColor=(33,150,243), textColor=(0,0,0), 

               hoverColor=(63,180,243), clickColor=(93,200,243), textHoverColor=None, borderHoverColor=None,

               borderWidth=1, borderColor=(0,0,0), borderRadius=0,
               
               font='Arial', fontSize=16, clickSink=1,
               
               text="Button", id=None, content=None):
    
    # Location
    self.x = x
    self.y = y

    # Size
    self.width = width
    self.height = height

    # Border
    self.borderWidth = borderWidth
    self.borderRadius = borderRadius
    self.borderColor = borderColor

    # If the border changes color on hovering then use new color, 
    # otherwise set it to just border color.
    if borderHoverColor == None:
      self.borderHoverColor = self.borderColor
    else:
       self.borderHoverColor = borderHoverColor

    # Colors
    self.backgroundColor = backgroundColor
    self.hoverColor = hoverColor
    self.clickColor = clickColor

    # Sink effect
    self.clickSink = clickSink
    self.currentSink = 0

    # Mouse click/hover logic
    self.mouseLogic = MouseClick()

    # Which cursor to display when hovering
    self.cursor = "hand"

    # Type of element this is
    self.type = "Button"


  def run(self, screen, mouse):

    # The package with information that is to be returned to the main loop if needed
    returnPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":None, "id":None, "type":self.type}

    # Check for hover and click
    self.mouseLogic.run((self.x, self.y), (self.width, self.height), mouse)

    # If hovering queue a change in cursor
    if self.mouseLogic.hoverTest == True:
      returnPackage["changeCursor"] = True

    # If triggered queue a trigger to be sent up to main loop
    if self.mouseLogic.isTriggered == True:
      returnPackage["triggered"] = True

    # Adds a sinking effect to the button when clicked down
    if self.mouseLogic.clickDownTest == True:
      self.currentSink = self.clickSink 
    else:
      self.currentSink = 0 

    # Draw the button
    if self.mouseLogic.clickDownTest == True:
      self.drawButton(screen, self.clickColor, self.borderHoverColor)
    elif self.mouseLogic.hoverTest == True:
      self.drawButton(screen, self.hoverColor, self.borderHoverColor)
    else:
      self.drawButton(screen, self.backgroundColor, self.borderColor)


    return returnPackage


  def drawButton(self, screen, color, bord_col):

    # Draw the border
    pygame.draw.rect(screen, bord_col, (self.x, self.y+self.currentSink, 
                                        self.width, self.height), border_radius=self.borderRadius)

    # Draw the button
    pygame.draw.rect(screen, color, (self.x+self.borderWidth, self.y+self.borderWidth+self.currentSink, 
																		 self.width-self.borderWidth*2, self.height-self.borderWidth*2), border_radius=self.borderRadius)