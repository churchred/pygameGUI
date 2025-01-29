
# Churchred's GUI library for Pygame

## Summary

This is a simple GUI library I made to use in Pygame. 
It is designed to make designing an app easier, so you can keep your focus on the app logic.


## Set-up

  To set everthing up you first need to import the library.

    ```
     from churchred_gui import *

    ```

    

  Then all you need to do is make the screen, and to create a basic loop for it.
  The logic for what happens when a module -like a button- is clicked should go inside the if-statement.
  The *package* variable will contain information about the triggered module.

    ```

    window = Screen()
    while True:

      window.run()
      
      if window.elementPackage['triggered'] == True:
        print(window.elementPackage)

    ```
  
  `elementPackage = {"changeCursor":False, "cursor":self.cursor, "triggered":False, "content":None, "id":None, "type":Button }`
  <br>

  We can ingore the first three of these elements:
  * `changeCursor:` Is true if we need to change the cursor. 
  * `cursor:` What we should change the cursor into (arrow, hand etc.)
  * `triggered:` Is when an item in activated, such as a button click, or pressing enter in a input field

  But the rest are very useful, and are the bread and butter of the logic loop:
  * `content:` May contain content you wish to use when an element is triggered. Example: The text within a triggered input field.
  * `id:` For when you want a link a certian action or function to a spesific element (such as a button to a function)
  * `type:` Is the type of object that has been triggered. (Button, Slider, etc.)<br><br>

    
# Modules
This library contains many different modules. 
Each module has many possible settings and functions that can be useful.
Most variables should NOT be changed post creation. Colors are usually fine however.

**Current modules**
* Window
* Button

## Window:

### Variables

* **width:** Width of the window
* **height:** Height of the window 
* **backgrounColor:** Background color of the window. (RBG)
  > Note that the library comes with predefined colors. See `settings.py`.
* **title:** The text on the banner of the app.
* **FPS:** Default value is 60. It's the framerate cap.
* **showFPS:** True/False. If True it will display the apps FPS in the banner next to the title.
* **appMessages:** True/False. Allows the GUI to print messages about events. (example: prints new size when resizing)

* **resizable:** Wether or not you are able to change the size of the window.
* **minWidth:** Minimum possible width for the window. Only used when resizing the window. 
* **minHeight:** Minimum possible height for the window. Only used when resizing the window. 
* **maxWidth:** Maximum possible width for the window. Only used when resizing the window. 
* **maxHeight:** Maximum possible height for the window. Only used when resizing the window. 
  > Note that the maximum and minimum values only stops the size from going outside of bounds when the user is resizing the window. If width is already beyond the scope upon creation, then it wont be fixed until the next time the window is resized.



### Functions
* **addElements():** Can take multiple arguments. When you have created a component, such as a button, you can add it to the window using this function.