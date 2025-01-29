

from churchred_gui import *


# Todo list: Make Z-index and overlap in general work
# Only the top button should be pressed when two overlap.
# The one with the highest Z-index should be overlapping when two items overlap

# Add general Modul class and Click class, and HOLD class


window = Window(resizable=True, backgrounColor=colorIndex["greenDark"])
btn = Button(y=100)
btn2 = Button(y=200)
btn3 = Button(y=300)
btn4 = Button(y=400)
btn5 = Button(y=100, x=200)
btn6 = Button(y=200, x=200)
btn7 = Button(y=300, x=200)
btn8 = Button(y=400, x=200)

window.addElements(btn, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

while True:

  window.run()



    
