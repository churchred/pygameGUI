


import pygame
from .mouseClick import MouseClick


class buttonText():
  def __init__(self,    
               width, height, text="Text",
               textColor=(0,0,0), font="Arial", fontSize=20,
               underline=False, capitalize=False, toLowerCase=False, toUpperCase=False
               ):
    
    # Text to be printet
    self.text = text

    # Canvas size, used to center the text, i.e text background
    self.width = width
    self.height = height

    # Text appearance
    self.font = font
    self.fontSize = fontSize
    self.textColor = textColor

    # Text decoration
    self.transformText = {
      "underLine"  : underline,
      "capitalize" : capitalize,
      "toLowerCase": toLowerCase,
      "toUpperCase": toUpperCase
    }

    self.setText(self.text)
  
  def setText(self, text):

    # Makes a new element so we dont change the given text, 
    # just in case we need it fresh at somepoint
    self.prossesedText = text

    # Adds text transformations
    if self.transformText['capitalize'] == True:
      self.prossesedText = text.capitalize()
    if self.transformText['toUpperCase'] == True:
      self.prossesedText = text.upper()
    if self.transformText['toLowerCase'] == True:
      self.prossesedText = text.lower()

    # Making the text and getting it's size
    self.myFont = pygame.font.SysFont(self.font, self.fontSize)

    # Makes the text element
    self.textElement = self.myFont.render(self.prossesedText, 1, (self.textColor))

    # Get size of text element
    self.textWidth, self.textHeight = self.textElement.get_width(), self.textElement.get_height()

  def run(self, screen, location):

    # Centers the text within the button element
    x = location[0] + (self.width)/2 - self.textWidth/2
    y = location[1] + (self.height)/2 - self.textHeight/2

    # Draws the text
    screen.blit(self.textElement, (x, y))

    # Adds underline if neeeded
    if self.transformText['underLine'] == True:
      pygame.draw.rect(screen, self.textColor, (x, y+self.textHeight*0.9, self.textWidth, 1))



class Button():
  def __init__(self, 
               x=0, y=0, width=100, height=30,

               backgroundColor=(33,150,243), textColor=(0,0,0), 

               hoverColor=(63,180,243), clickColor=(93,200,243), textHoverColor=None, borderHoverColor=None,

               borderWidth=1, borderColor=(0,0,0), borderRadius=0,
               
               font='Arial', fontSize=20, clickSink=1,
               
               capitalize=False, toLowerCase=False, toUpperCase=False, underLine=False,
               
               text="Button", id=None, content=None, zIndex=0):
    



    # Location
    self.x = x
    self.y = y

    # Size
    self.width = width
    self.height = height

    # Store text-related attributes in a dictionary
    self.textParams = {
        "text": text, "width": self.width, "height": self.height,
        "font": font, "fontSize": fontSize, "textColor": textColor,
        "capitalize": capitalize, "toLowerCase": toLowerCase, 
        "toUpperCase": toUpperCase, "underline": underLine
    }

    # Make the text elements
    self.textHoverColor = textHoverColor
    self.textColor = textColor
    self.setText(text)


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

    # zIndex
    self.zIndex = zIndex

    # ID and content
    self.id = id
    self.content = content


  def run(self, screen, mouse):

    # The package with information that is to be returned to the main loop if needed
    returnPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":self.content, "id":self.id, "type":self.type}

    # Check for hover and click
    self.mouseLogic.run((self.x, self.y), (self.width, self.height), mouse)

    # If hovering queue a change in cursor
    if self.mouseLogic.hoverTest == True:
      returnPackage["changeCursor"] = True

    # If triggered queue a trigger to be sent up to main loop
    if self.mouseLogic.isTriggered == True:
      returnPackage["triggered"] = True

    return returnPackage


  def draw(self, screen):

    # Adds a sinking effect to the button when clicked down
    if self.mouseLogic.clickDownTest == True:
      self.currentSink = self.clickSink 
    else:
      self.currentSink = 0 

    # Draw the button base on wether its being clicked, hovered, or just default.
    if self.mouseLogic.clickDownTest == True:
      self.drawButton(screen, self.clickColor, self.borderHoverColor)
    elif self.mouseLogic.hoverTest == True:
      self.drawButton(screen, self.hoverColor, self.borderHoverColor)
    else:
      self.drawButton(screen, self.backgroundColor, self.borderColor)

    # If we need text color to change on hover we print that text element instead
    # Otherwise we print the normal one
    if self.mouseLogic.hoverTest == True and self.textHoverColor != None:
      self.textElementHover.run(screen, (self.x, self.y+self.currentSink))
    else:
      self.textElement.run(screen, (self.x, self.y+self.currentSink))

  def drawButton(self, screen, color, bord_col):

    # Draw the border
    pygame.draw.rect(screen, bord_col, (self.x, self.y+self.currentSink, 
                                        self.width, self.height), border_radius=self.borderRadius)

    # Draw the button
    pygame.draw.rect(screen, color, (self.x+self.borderWidth, self.y+self.borderWidth+self.currentSink, 
																		 self.width-self.borderWidth*2, self.height-self.borderWidth*2), border_radius=self.borderRadius)
    

  def setText(self, text):
      
      # Changes the text paramaters to what we want
      self.textParams["text"] = text
      self.textParams["textColor"] = self.textColor

      # Create text elements
      self.textElement = buttonText(**self.textParams)  # Unpacking dictionary

      # If we need another text element for hovering, we make it as well
      if self.textHoverColor is not None:
          self.textParams["textColor"] = self.textHoverColor
          self.textElementHover = buttonText(**self.textParams)