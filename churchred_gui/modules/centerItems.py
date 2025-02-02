
from .settings import directions


class CenterItems():
  def centerElements(self, elements, start_x, start_y, container_width, container_height, direction):
          
    # If empty do nothing
    if not elements:
        return 

    # Center horizontally
    if direction in directions[0]:  
        
        # Calulate total width of all elements
        total_width = sum(item.width for item in elements)
        
        # Find avaliable space between each element
        space_available = container_width - total_width
        space_between_x = space_available / (len(elements) + 1)

        # The position for the first element
        x_position = space_between_x + start_x

        # Place all elements in their new position
        for item in elements:
            item.x = x_position
            item.y = start_y + (container_height - item.height) / 2 
            x_position += item.width + space_between_x


    # Center vertically
    elif direction in directions[1]: 
        
        # Calulate total height of all elements
        total_height = sum(item.height for item in elements)

        # Find avaliable space between each element
        space_available = container_height - total_height
        space_between_y = space_available / (len(elements) + 1)

        # The position for the first element
        y_position = space_between_y + start_y

        # Place all elements in their new position
        for item in elements:
            item.y = y_position
            item.x = start_x + (container_width - item.width) / 2  
            y_position += item.height + space_between_y

    
    # Centers internal pieces of things
    for item in elements:
        item.center()
