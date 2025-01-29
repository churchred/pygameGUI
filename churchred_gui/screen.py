
# Import pygame reletated things
import pygame, sys
from churchred_gui.setings import mouseCursor

class Screen():
  def __init__(self,
               width=500, height=500, FPS=60, 
               minWidth = 200, minHeight = 150,
               backgrounColor = (255,255,255),
               title="Application", showFPS=True, resizable = False
               ):


    # Pygame stuff
    pygame.init()                 
    pygame.font.init()  

    # If testing, and we dont want something to happen,
    # and we show FPS in title.
    self.showFPS = showFPS
    self.title = title

    # Screen size
    self.width = width
    self.height = height
    self.FPS = FPS

    # Resize variables
    self.minWidth =  minWidth
    self.minHeight = minHeight
    self.resizeable = resizable

    # Background color
    self.backgrounColor = backgrounColor

    # Makes the app screen
    if self.resizeable == False:
      self.screen = pygame.display.set_mode((self.width, self.height)) 
    if self.resizeable == True:
      self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) 

    # Makes the game tick
    self.clock = pygame.time.Clock()

    # Makes the event triggers
    self.event = []


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

      
    # Gather basic data
    self.dt = self.clock.tick(self.FPS) / 1000   # Delta time. Used for smooth animations
    self.mouse = [pygame.mouse.get_pos(),        # Mouse position and pressed-state.
                  pygame.mouse.get_pressed()]
    

    # Turns pointer cursor back to arrow
    self.cursor = "arrow"
    pygame.mouse.set_cursor(mouseCursor[self.cursor])

    # Background color of app
    self.screen.fill(self.backgrounColor)


    # Update screen and clock
    self.clock.tick(self.FPS) # Default FPS Limit: 60

    # Checks which caption to set it the window-banner
    # If FPS is enabled we show current FPS.
    if self.showFPS == True:
      pygame.display.set_caption(self.title + "     -     FPS (" + str(int(self.clock.get_fps())) + ")")
    else:
      pygame.display.set_caption(self.title)


    # Updates the app window
    pygame.display.update()


  # The logic for screen resizing if enabled
  def resize_logic(self, event):
    
    # Set new screen size
    self.width, self.height = event.w, event.h
    
    # Stops the screen from being too small
    if self.width < self.minWidth:
      self.width = self.minWidth
    if self.height < self.minHeight:
      self.height = self.minHeight

    # Resize the window
    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    # Print new info about screen
    print(f"Resized window to: {self.width}x{self.height}")


  