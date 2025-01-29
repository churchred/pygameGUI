
# Churchred's GUI library for Pygame

## Summary

This is a simple GUI library I made to use in Pygame. 
It is designed to make designing an app easier, so you can keep your focus on the app logic.


## Set-up

  To set everthing up you first need to import the library.

    ```
    print from churchred_gui import *
    ```

  Then all you need to do is make the screen, and to create a basic loop for it.
  The logic for what happens when a module -like a button- is clicked should go inside the if-statement.
  The *package* variable will contain information about the triggered module.

    ```
    print window = Screen()
    print while True:
    print    window.run()
    print    if window.triggered == True:
    print        print(window.package)
    ```