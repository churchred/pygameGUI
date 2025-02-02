

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["orangeDark"])

label1 = Label(text="Fantastic Beast and Where to Find Them", fontSize=30)
label2 = Label(text="There are many cool magical beasts in Harry Potter", fontSize=20, cursor="hand", clickable=True)

btn = Button(y=100, id="green")
btn2 = Button(y=100, id="blue")
btn3 = Button(y=120, backgroundColor=colorIndex["purple"], underline=True)

fb = FlexBox(centerDirection=1, height=400, zIndex=3, x=20)
fb.addElements(btn2, btn3)

fb2 = FlexBox(backgroundColor=colorIndex["green"], y=90, zIndex=3)
fb2.addElements(btn)

window.addElements(fb, fb2)

while True:

  # Runs the pygame loop, and checks if somehting is triggered
  window.run()
  if window.elementPackage['triggered'] == True:

    # Prints information about triggered elemenet
    print(window.elementPackage)





    
