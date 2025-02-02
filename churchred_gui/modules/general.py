

# Function to lighten a color
def lightenColor(color, factor=0.2):
    
    # Create an empty list to store new colors
    lightened_color = []

    # Loop through each component (red, green, blue) in the color tuple
    for col in color:
        
        # Lighten the color by factor-precent
        lightened_value = int((1 + factor) * col)
        
        # Ensure the value does not exceed 255 (RGB components cannot be greater than 255)
        lightened_value = min(lightened_value, 255)
        
        # Append the new value to the list
        lightened_color.append(lightened_value)

    # Convert the list to a tuple and return it
    return tuple(lightened_color)



# Function to darken a color
def darkenColor(color, factor=0.2):
    
    # Create an empty list to store new colors
    darkened_color = []

    # Loop through each component (red, green, blue) in the color tuple
    for col in color:
        
        # Darken the color by factor-precent
        darkened_value = int(col * (1 - factor))
        
        # In case the value is less than zero
        darkened_value = max(darkened_value, 0)
        
        # Append the new value to the list
        darkened_color.append(darkened_value)

    # Convert the list to a touple and return it
    return tuple(darkened_color)