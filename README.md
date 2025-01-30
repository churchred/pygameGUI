
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
The most important element we can make. It is this that creates the window and all the window logic.
It is this element that contains all other modules.

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


## Button
A button. You can click it!
All of the variables have default values, so you dont need to use any them if you just want a quick button.
Don't change the variables after the object is created, unless you you do it through a button function, see section below.

### Variables
* **width:** Width of the button
* **height:** Height of the button
* **x:** Location of button on the x-axis
* **y:** Location of button on the y-axis

* **text:** The text you want to have on your button. The text is always centered within the button. If text is too long, there will be overflow.
* **id:** Button id, to give a spesific button a spesific function, we need to add an id to it. Deault None.
* **content:** You can add content to a button, any format, this is sent back to the main loop on a click. 
* **zIndex:** If there is overlap between multiple elements, the higher z-index is prioritized. Default for all moduls is 0.

* **borderWidth:** Width of the border around the button. Default is 0.
* **borderRadius:** How rounded the corners of the button should be. Default is 0.
* **clickSink:** How much  the buttons moves downwards when clicked down.

* **backgroundColor:** Color of the button
* **textColor:** Color of the button text
* **borderColor:** Color of the button border, if you have one.

* **hoverColor:** Color of the button when its being hovered
* **clickColor:** Color of the button when its being clicked down
* **textHoverColor:** Text color when button is being hovered. None by default.
* **borderHoverColor:** Color of the border, if you have one, when you are hovering the button

* **font:** Font of the button text. Arial by default.
* **fontSize:** Font size of the button text. 20 by default.

* **capitalize:** If you want to make each word of the text capitalized.
* **toLowerCase:** If you want the text in all lowercase.
* **toUpperCase:** If you want the text in all uppercase.
* **underLine:** If you want a underline beneath the text.

### Functions
* **setText():** Used to change button text.     