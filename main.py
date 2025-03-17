

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["orangeDark"], centerDirection="vert")

btn = Button(x= 50, y=100, id="green")

window.addElements(btn)

while True:

  # Runs the pygame loop, and checks if somehting is triggered
  window.run()
  if window.elementPackage['triggered'] == True:

    # Prints information about triggered elemenet
    print(window.elementPackage)





    
