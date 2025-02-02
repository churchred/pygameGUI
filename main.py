

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["greenDark"], centerDirection="vert")

btn = Button(x=10, y=300, zIndex=2, backgroundColor=colorIndex['red'], id='red')

btn2 = Button(y=100, id="blue", width=300, height=50, fontSize=30, toUpperCase=True)
btn3 = Button(y=120, backgroundColor=colorIndex["purple"], underline=True)


window.addElements(btn, btn2, btn3)

while True:

  # Runs the pygame loop, and checks if somehting is triggered
  window.run()
  if window.elementPackage['triggered'] == True:

    # Prints information about triggered elemenet
    print(window.elementPackage)

    # If button is clicked set new text to it
    if window.elementPackage["id"] == "red":
      btn.setText("Yoo")




    
