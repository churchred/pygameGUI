


import pygame
from .modules.mouseClick import MouseClick
from .modules.textLine import lineText
from .modules.UIElement import UIElement
from .modules.general import lightenColor, darkenColor

class Button(UIElement):
  def __init__(self, 
               
            # UI-element variables:
            x=0, y=0, width=100, height=30,
            id=None, type="Button", zIndex=0,
            content=None, clickable=True,

            # Text elements
            text = "Button", font="Arial", fontSize = 18,
            textColor = (0,0,0), underline=False, 
            capitalize=False, toLowerCase=False, toUpperCase=False,

            # Button spesific Elements
            backgroundColor=(33,150,243), hoverColor=None, clickColor=None, 
            borderWidth=1, borderColor=(0,0,0), borderHoverColor=None, borderRadius=0):
    
    # Sets the basic UI-element variables from UIElement-class
    super().__init__(x=x, y=y, width=width, height=height, clickable=clickable, cursor="hand",
                     type=type, id=id, zIndex=zIndex, content=content)

    # Border variables
    self.borderWidth = borderWidth
    self.borderRadius = borderRadius
    self.borderColor = borderColor

    # If the border changes color on hovering then use new color, 
    # otherwise set it to just border color.
    self.borderHoverColor = borderHoverColor or self.borderColor


    # Colors
    self.backgroundColor = backgroundColor
    self.hoverColor = hoverColor if hoverColor is not None else lightenColor(backgroundColor)
    self.clickColor = clickColor if clickColor is not None else darkenColor(self.hoverColor)

    # Sink effect
    self.maxSink = 1
    self.currentSink = 0

    # Make button text
    self.text = lineText(text=text, font=font, fontSize=fontSize, textColor=textColor,
                         underline=underline, toUpperCase=toUpperCase, toLowerCase=toLowerCase,
                         capitalize=capitalize, width=self.width, height=self.height)


  def draw(self, screen, dt):

    # Adds a sinking effect to the button when clicked down
    if self.mouseLogic.clickDownTest == True:
      self.currentSink = self.maxSink 
    else:
      self.currentSink = 0 

    # Draw the button base on wether its being clicked, hovered, or just default.
    if self.mouseLogic.clickDownTest == True:
      self.drawButton(screen, self.clickColor, self.borderHoverColor)
    elif self.mouseLogic.hoverTest == True and self.clickable == True:
      self.drawButton(screen, self.hoverColor, self.borderHoverColor)
    else:
      self.drawButton(screen, self.backgroundColor, self.borderColor)

    self.text.run(screen, (self.x, self.y+self.currentSink))


  def drawButton(self, screen, color, bord_col):

    # Draw the border
    pygame.draw.rect(screen, bord_col, 
    (self.x, self.y+self.currentSink, self.width, self.height), border_radius=self.borderRadius)

    # Draw the button
    pygame.draw.rect(screen, color, 
    (self.x+self.borderWidth, self.y+self.borderWidth+self.currentSink, 
		self.width-self.borderWidth*2, self.height-self.borderWidth*2), border_radius=self.borderRadius)

  def setText(self, text):
    self.text.setText(text=text)