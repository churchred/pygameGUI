



class MouseClick():
  def __init__(self, clickable):


    self.hoverTest = False     # Check if we are hovering
    self.clickDownTest = False # If mouse button is clicked down while we are hovering
    self.inititalClick = False # If the initially clicked the mouse button down while within the element
    self.allowClick = False    # See if we are allowed to initially click element (i.e mouse not clicked while hovering element)

    # Can we click it?
    self.clickable = clickable

    # If element is clicked this becomes true for a single frame
    self.isTriggered = False


  def run(self, elementSize, elementPosition, mouse):

    # Reset the triggered varible so it only runs once
    self.isTriggered = False

    if not self.clickable:
      # Check if cursor is hovering element
      self.hoverCheck(elementSize, elementPosition, mouse)
      return

    # Check if we release the mouse button while within the element
    self.clickReleaseCheck(elementSize, elementPosition, mouse)

    # Check if cursor is hovering element
    self.hoverCheck(elementSize, elementPosition, mouse)

    self.clickDownCheck(mouse)

    if self.hoverTest and not mouse[1][0]:
      self.allowClick = True
    elif not self.hoverTest:
      self.allowClick = False

    if self.allowClick and mouse[1][0]:
      self.inititalClick = True
    if not mouse[1][0]:
      self.inititalClick = False


  def clickDownCheck(self, mouse):
    if self.hoverTest and mouse[1][0] and self.inititalClick:
      self.clickDownTest = True
    else:
      self.clickDownTest = False
  
  # Check if we are hovering the element or not
  def hoverCheck(self, elementPosition, elementSize, mouse):

    # Unpacks given variables for more readability
    x, y = elementPosition
    width, height = elementSize
    mouse_x, mouse_y = mouse[0]

    # Check if mouse if within bounds of the element
    self.hoverTest = (x < mouse_x < x + width) and (y < mouse_y < y + height)


  # Check for button release if we are hovering and have clicked the button down
  # Then reset and re-check hover, because we might still be hovering
  def clickReleaseCheck(self, elementSize, elementPosition, mouse):
    if self.hoverTest and self.inititalClick:
      if not mouse[1][0]:
        self.isTriggered = True
        self.resetChecks()
        self.hoverCheck(elementSize, elementPosition, mouse)


  # Resets all the checks
  def resetChecks(self):
    self.hoverTest = False
    self.clickDownTest = False
  