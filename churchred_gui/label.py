import pygame
from .modules.textLine import lineText
from .modules.UIElement import UIElement
from .modules.mouseClick import MouseClick

class Label(UIElement):
  def __init__(self, 
              # UI-element variables:
              x=0, y=0, width=0, height=0,
              id=None, type="Label", zIndex=0,
              content=None, cursor="arrow", clickable=False,

              # Text elements
              text = "Button", font="Arial", fontSize = 18,
              textColor = (0,0,0), underline=False, 
              capitalize=False, toLowerCase=False, toUpperCase=False,
              
              # Label variables
              backgroundColor=None, borderColor=(0,0,0), borderRadius=0, borderWidth=1,
              padding=8):

    # Sets the basic UI-element variables from UIElement-class
    super().__init__(x=x, y=y, width=width, height=height, cursor="hand", clickable=clickable,
                     type=type, id=id, zIndex=zIndex, content=content)

    # Text element
    self.text = lineText(text=text, font=font, fontSize=fontSize, textColor=textColor,
                         underline=underline, toUpperCase=toUpperCase, toLowerCase=toLowerCase,
                         capitalize=capitalize, width=self.width, height=self.height)
    
    if not self.width:
      self.width, self.height = self.text.textWidth, self.text.textHeight
      self.text.width, self.text.height = self.width, self.height


    # Background color
    self.backgroundColor = backgroundColor
    self.padding = padding
    
    # Border variables
    self.borderColor = borderColor
    self.borderWidth = borderWidth
    self.borderRadius = borderRadius
    



  def draw(self, screen, dt):

    # Draw the label background if one is present
    self.drawRect(screen, self.backgroundColor, self.borderColor)

    # Draw the text
    self.text.run(screen, (self.x, self.y))


  def drawRect(self, screen, color, bord_col):

    if not self.backgroundColor:
      return

    # Draw the border
    pygame.draw.rect(screen, bord_col, 
    (self.x, self.y, self.width, self.height), border_radius=self.borderRadius)

    # Draw the background
    pygame.draw.rect(screen, color, 
    (self.x+self.borderWidth, self.y+self.borderWidth, 
		self.width-self.borderWidth*2, self.height-self.borderWidth*2), border_radius=self.borderRadius)