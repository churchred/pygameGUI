

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["orangeDark"])

label1 = Label(text="Fantastic Beast and Where to Find Them", fontSize=30, zIndex=10)
label2 = Label(text="There are many cool magical beasts in Harry Potter", fontSize=20, cursor="hand", clickable=True)

btn = Button(y=100, id="green")
btn2 = Button(y=100, id="blue")
btn3 = Button(y=120, backgroundColor=colorIndex["purple"], underline=True)

fb = FlexBox(centerDirection=1, height=400, zIndex=3, x=20, backgroundColor=colorIndex["black"])

fb2 = FlexBox( y=90, zIndex=3, centerDirection=1)
fb2.addElements(btn)

fb3 = FlexBox(backgroundColor=colorIndex["red"], width = 300, centerDirection=0)
fb3.addElements(btn3)


fb.addElements(fb2, fb3)

window.addElements(label1, fb)

while True:

  # Runs the pygame loop, and checks if somehting is triggered
  window.run()
  if window.elementPackage['triggered'] == True:

    # Prints information about triggered elemenet
    print(window.elementPackage)





    
