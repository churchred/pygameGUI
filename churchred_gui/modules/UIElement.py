
from .mouseClick import MouseClick

# General varibales all modules need
class UIElement:
    
    def __init__(self, 
        x=0, y=0, width=10, height=10,
        id=None, type=None, zIndex=0,
        content=None, clickable=False, cursor="arrow"
        ):

        # Location
        self.x = x
        self.y = y

        # Size
        self.width = width
        self.height = height

        # UI-logic variables
        self.id = id
        self.type = type
        self.zIndex = zIndex
        self.content = content

        # Which cursor to display when hovering
        self.clickable = clickable
        self.cursor = cursor
        if clickable == False:
            self.cursor = "arrow"

        # Mouse click/hover logic
        self.mouseLogic = MouseClick(self.clickable)
    

    def run(self, screen, mouse):
        
        # The package with information that is to be returned to the main loop if needed
        self.returnPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":self.content, "id":self.id, "type":self.type}

        # Check for hover and click
        self.mouseLogic.run((self.x, self.y), (self.width, self.height), mouse)

        # If hovering queue a change in cursor
        if self.mouseLogic.hoverTest == True:
            self.returnPackage["changeCursor"] = True

        # If triggered queue a trigger to be sent up to main loop
        if self.mouseLogic.isTriggered == True:
            self.returnPackage["triggered"] = True

        self.extraRunCode()

        return self.returnPackage
    
    def extraRunCode(self):
        pass

    def center(self):
        pass