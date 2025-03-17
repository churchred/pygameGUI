import pygame
from .modules.centerItems import CenterItems

class FlexBox(CenterItems):
  def __init__(self, 
      
          x=0, y=0, width=100, height=100,
          backgroundColor=None, borderColor=(0,0,0), borderRadius=0, borderWidth=1,
          centerDirection=0, zIndex=0):

    self.x = x
    self.y = y

    self.width = width
    self.height = height
    self.borderRadius = borderRadius
    self.borderWidth = borderWidth

    self.zIndex = zIndex
    self.type = "FlexBox"
    self.borderColor = borderColor

    self.backgroundColor = backgroundColor
    self.cursor = "arrow"

    self.screenElements = []
    self.centerDirection = centerDirection


  def run(self, screen, mouse):

    # The package with information that is to be returned to the main loop if needed
    returnPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":None, "id":None, "type":"FlexBox"}

    targetElement = None

    # Loop through and do the logic for each element, when we notice a hover we break loop.
    for element in self.screenElements:
      temp_package = element.run(screen, mouse)

      # If we are hovering an element then queue a change in the cursor
      if temp_package['changeCursor'] == True:
        targetElement = element
        returnPackage["changeCursor"] = True
        returnPackage["cursor"] = temp_package["cursor"]
        
      # If an element is triggered
      if temp_package['triggered'] == True:
        returnPackage['triggered'] = temp_package['triggered']
        returnPackage['id'] = temp_package['id']
        returnPackage['content'] = temp_package['content']
        returnPackage['type'] = temp_package['type']

      # If we are hovering something after the check then we dont need to check any other element.
      # This is to stop logic from running on the bottom element when two or more are overlapping.
      if targetElement != None:
        break

    # Reset other non-hovered elements
    for element in self.screenElements:
      if element != targetElement and element.type != "FlexBox":
        element.mouseLogic.resetChecks()
    
    return returnPackage


  def draw(self, screen, dt):
    
    # Draw a rect with the background color if applicable
    if self.backgroundColor != None:
      self.drawRect(screen, self.backgroundColor, self.borderColor)

    # Loop through the list of objects and draw them onto the screen
    for element in reversed(self.screenElements):
      element.draw(screen, dt)


  def addElements(self, *args):
    for item in args:
      self.screenElements.append(item)

    # Sort by Z-index, where highest is placed at the top of list
    self.screenElements.sort(key=lambda x: x.zIndex, reverse=True)

    # Center items if needed
    self.center()



  # When centering content, this should happen
  def center(self):

    # elements, container_width, container_height, direction
    self.centerElements(self.screenElements, self.x, self.y, self.width, self.height, self.centerDirection)



  def drawRect(self, screen, color, bord_col):

    # Draw the border
    pygame.draw.rect(screen, bord_col, 
    (self.x, self.y, self.width, self.height), border_radius=self.borderRadius)

    # Draw the button
    pygame.draw.rect(screen, color, 
    (self.x+self.borderWidth, self.y+self.borderWidth, 
		self.width-self.borderWidth*2, self.height-self.borderWidth*2), border_radius=self.borderRadius)