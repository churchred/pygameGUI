
# Import pygame reletated things
import pygame, sys
from churchred_gui.setings import mouseCursor

class Window():
  def __init__(self,
               width=500, height=500, FPS=60, 
               minWidth = None, minHeight = None,
               maxWidth = None, maxHeight = None,
               backgrounColor = (255,255,255),
               title="Application", showFPS=True, resizable = False,
               appMessages = True
               ):


    # Pygame stuff
    pygame.init()                 
    pygame.font.init()  

    # For testing
    self.showFPS = showFPS         # Shows the current FPS in the banner
    self.appMessages = appMessages # Allows print-messages from the GUI

    # Screen size
    self.title = title
    self.width = width
    self.height = height
    self.FPS = FPS

    # Resize variables
    self.resizeable = resizable
    self.minWidth =  minWidth
    self.minHeight = minHeight
    self.maxWidth = maxWidth
    self.maxHeight = maxHeight

    # Background color
    self.backgrounColor = backgrounColor

    # Makes the app screen
    if self.resizeable == False:
      self.screen = pygame.display.set_mode((self.width, self.height)) 
    if self.resizeable == True:
      self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) 

    # Makes the game tick
    self.clock = pygame.time.Clock()

    # Makes the cursor variable
    self.cursor = {'old' : None, 'new' : 'arrow'}

    # Contains the screen elements (i.e buttons, sliders etc.)
    self.screenElements = []

    # If something is activated or "triggered" on the screen
    self.isTriggered = False


  # Runs the app
  def run(self):

    # This loop runs everytime pygame catches
    # an event. Such as, keypress, exit, mousewheel.
    for event in pygame.event.get(): 

      # What happens if we exit the app
      if event.type == pygame.QUIT:   
        pygame.quit()
        sys.exit()

      # What happens if we resize the app window
      if event.type == pygame.VIDEORESIZE:
        self.resize_logic(event)

    # Reset Trigger variable
    self.isTriggered = False

    # Gather basic data
    self.mouse = [pygame.mouse.get_pos(),        # Mouse position and pressed-state.
                  pygame.mouse.get_pressed()]
    


    # Background color of app
    self.screen.fill(self.backgrounColor)

    # Queue a change in cursor back to an arrow
    self.cursor['new'] = 'arrow'

    # The package of information about an object to be returned to main loop
    self.elementPackage = {'triggered'  : False}

    # Loop through and draw all the elements on the screen ----------------------
    for element in self.screenElements:
      temp_package = element.run(self.screen, self.mouse)

      # If we are hovering an element then queue a change in the cursor
      if temp_package['changeCursor'] == True:
        self.cursor['new'] = temp_package['cursor']

      # If an element is triggered
      if temp_package['triggered'] == True:
        self.elementPackage = temp_package

    # Change cursor based on given data. Change only occurs if new cursor is different from current one.
    if self.cursor['new'] != self.cursor['old']:
      pygame.mouse.set_cursor(mouseCursor[self.cursor['new']])
      self.cursor['old'] = self.cursor['new']
    

    # Checks which caption to set it the window-banner
    # If FPS is enabled we show current FPS.
    if self.showFPS == True:
      pygame.display.set_caption(self.title + "     -     FPS (" + str(int(self.clock.get_fps())) + ")")
    else:
      pygame.display.set_caption(self.title)

    # Update screen and clock
    self.clock.tick(self.FPS) 
    pygame.display.update()


  # To add one or more elements to the screen
  def addElements(self, *args):
    for item in args:
      self.screenElements.append(item)


  # The logic for screen resizing if enabled
  def resize_logic(self, event):
    
    # Set new screen size
    self.width, self.height = event.w, event.h
    
    # Stops the screen from being too small
    if self.minWidth != None:
      if self.width < self.minWidth:
        self.width = self.minWidth
    if self.minHeight != None:
      if self.height < self.minHeight:
        self.height = self.minHeight

    # Stops the screen from becoming too big
    if self.maxHeight != None:
      if self.height > self.maxHeight:
        self.height = self.maxHeight
    if self.maxWidth != None:
      if self.width > self.maxWidth:
        self.width = self.maxWidth

    # Resize the window
    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    # Print new info about screen if able
    if self.appMessages == True:
      print(f"Resized window to: {self.width}x{self.height}")


  