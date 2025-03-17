import pygame
from .modules.UIElement import UIElement
from .modules.toggleHandle import toggleHandle

class Toggle(UIElement):
  def __init__(self, 
            # UI-element variables:
            x=0, y=0, width=75, height=45,
            id=None, zIndex=0,

            # Toggle spesific Elements
            backgroundColor = (204,204,204), 
            backgroundColorActive = (33,150,243),
            handleColor = (250,250,250),
            toggleSpeed = 200):
    
    # Toggle on or off
    self.status = 0

    # Sets the basic UI-element variables from UIElement-class
    super().__init__(x=x, y=y, width=width, height=height, clickable=True, cursor="hand",
                     type="Toggle", id=id, zIndex=zIndex, content=self.status)

    # The two colors we use (Is set by the self.status)
    self.backgroundColor = {"0" : backgroundColor, "1" : backgroundColorActive}

    # Speed of the handle
    self.toggleSpeed = toggleSpeed

    # Padding to keep handle from touching sides.
    self.padding = 5

    # Handle object
    self.handle = toggleHandle(self.width, self.height, self.padding, handleColor)



  def draw(self, screen, dt):

    # Draw the background
    pygame.draw.rect(screen, self.backgroundColor[str(self.status)], (self.x, self.y, self.width, self.height))

    # Draw the handle
    self.handle.draw(screen, self.x, self.y, self.height)

    # If it has been triggered, and the lock is in place, then move the handle
    if self.mouseLogic.clickable == False:
      self.moveHandle(dt)


  # If toggle is clicked
  def extraRunCode(self):
    if self.mouseLogic.isTriggered == True:
      self.mouseLogic.clickable = False
      self.returnPackage["content"] = self.status^1

  def moveHandle(self, dt):
    
    # Turn the toggle ON
    if self.status == 0:
      if self.x + self.handle.x + self.handle.width + self.padding + self.toggleSpeed * dt < self.x + self.width:
        self.handle.x += self.toggleSpeed * dt
      else:
        self.toggleStatus(self.width - self.handle.width - self.padding)
    
    # Turn the toggle OFF
    elif self.status == 1:
      if self.x + self.handle.x - self.padding - self.toggleSpeed * dt > self.x:
        self.handle.x -= self.toggleSpeed * dt
      else:
        self.toggleStatus(self.padding)

  def toggleStatus(self, x):
    self.handle.x = x
    self.mouseLogic.clickable = True
    self.status ^= 1