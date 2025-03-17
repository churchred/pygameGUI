

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["orangeDark"], centerDirection="vert")

btn1 = Button(id="1", text="Button 1", backgroundColor=colorIndex["redDark"])
btn2 = Button(id="2", text="Button 2")
flx = FlexBox(width=300)
flx.addElements(btn1, btn2)

tog = Toggle()
txt = Label(text="Hello There!")
window.addElements(txt, flx, tog)

while True:

  # Runs the pygame loop, and checks if somehting is triggered
  window.run()
  if window.elementPackage['triggered'] == True:

    # Prints information about triggered elemenet
    print(window.elementPackage)

    if window.elementPackage['content'] == 1:
      window.backgrounColor = colorIndex["grey"]
    if window.elementPackage['content'] == 0:
      window.backgrounColor = colorIndex["orangeDark"]



    
