
import pygame

class toggleHandle():
  def __init__(self, width, height, padding, color):
    
    self.x = padding
    self.height = height - padding*2
    self.width = width / 2.2
    self.backgroundColor = color

  def setCoordiantes(self, x, y):
    pass

  def draw(self, screen, x, y, height):

    # Draw the button
    pygame.draw.rect(screen, self.backgroundColor, 
    (self.x+x, y+height/2-self.height/2, 
     self.width, self.height))