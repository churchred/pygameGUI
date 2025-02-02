


# General varibales all modules need
class UIElement:
    
    def __init__(self, 
        x=0, y=0, width=10, height=10,
        id=None, type=None, zIndex=0,
        content=None, cursor=None
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
        self.cursor = cursor
        