

class MouseClick():
  def __init__(self):

    # The two tests for checking for a click
    self.hoverTest = False
    self.clickDownTest = False

    # If element is clicked this becomes true for a single frame
    self.isTriggered = False


  def run(self, elementSize, elementPosition, mouse):

    # Reset the triggered varible so it only runs once
    self.isTriggered = False

    # Check if cursor is hovering element
    self.hoverCheck(elementSize, elementPosition, mouse)

    # Check if we click down the mouse button while within the element
    self.clickDownCheck(mouse)

    # Check if we release the button again WHILE the two previous checks are true
    self.clickReleaseCheck(mouse)
    
  
  # Check if we are hovering the element or not
  def hoverCheck(self, elementPosition, elementSize, mouse):

    x, y = elementPosition
    width, height = elementSize

    # See if mouse is within the element and NOT already clicked down when it is.
    if mouse[0][0] > x and mouse[0][0] < x + width and mouse[0][1] > y and mouse[0][1] < y + height:
      if mouse[1][0] == False:
        self.hoverTest = True
    else:
      self.resetChecks()


  # See if we click the mouse button down while the hover test is true  
  def clickDownCheck(self, mouse):
    if self.hoverTest == True:
      if mouse[1][0] == True:
        self.clickDownTest = True

  # Check for button release if we are hovering and have clicked the button down
  def clickReleaseCheck(self, mouse):
    if self.hoverTest == True and self.clickDownTest == True:
      if mouse[1][0] == False:
        self.isTriggered = True
        self.resetChecks()

  # Resets all the checks
  def resetChecks(self):
    self.hoverTest = False
    self.clickDownTest = False

    
  
  