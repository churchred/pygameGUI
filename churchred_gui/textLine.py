import pygame



class lineText():
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

    # Baseline to highest point, used to position underline
    self.font_ascent = self.myFont.get_ascent() 

  def run(self, screen, location):

    # Centers the text within the button element
    x = location[0] + (self.width)/2 - self.textWidth/2
    y = location[1] + (self.height)/2 - self.textHeight/2

    # Draws the text
    screen.blit(self.textElement, (x, y))

    # Draw an underline underneat if needed
    if self.transformText['underLine']:
      underline_y = y + self.font_ascent + 2  # Position just below the baseline
      pygame.draw.line(screen, self.textColor, 
                        (x, underline_y), (x + self.textWidth, underline_y), 1)

