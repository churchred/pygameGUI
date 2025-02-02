# Churchred's GUI Library for Pygame

## Overview

Churchred's GUI library is a simple and efficient tool designed to streamline GUI development in Pygame. It allows developers to focus on app logic while handling interface elements with ease.

---

## Installation

First, import the library into your Pygame project:

```python
from churchred_gui import *
```

---

## Creating a Window

To initialize a basic GUI, create a window instance and run the main loop:

```python
window = Screen()

while True:
    window.run()
    
    if window.elementPackage['triggered']:
        print(window.elementPackage)
```

The `elementPackage` dictionary contains details about triggered elements:

```python
{
    "triggered": False,  # Indicates if an element was interacted with
    "content": None,  # Stores relevant content (e.g., text from an input field)
    "id": None,  # Identifies specific elements
    "type": 'Button'  # Specifies the type of element triggered
}
```

---

## Modules

The library provides several GUI elements, each with customizable attributes and functions. Most properties should not be modified after creation, except for color-related attributes. However, text colors need to be re-rendered.

It's not made to be used in games, but instead to be used for simple app development in pygame.

### Available Modules

- **Window** (Core container for all elements)
- **Button** (Clickable UI component)

---

## Window

The **Window** module is the primary element that manages the GUI environment.

### Attributes

- **width** *(int)* - Window width.
- **height** *(int)* - Window height.
- **backgroundColor** *(RGB)* - Background color. Predefined colors are available in `settings.py`.
- **title** *(str)* - Window title text.
- **FPS** *(int, default: 60)* - Frame rate cap.
- **showFPS** *(bool)* - Displays FPS in the title bar if `True`.
- **centerDirection** *(0/1, "horizontal"/"hor", "vertical"/"vert", default: None)* - Determines how elements inside the window are arranged.
  - `0`, `"hor"`, `"horizontal"`: Arrange elements in a **horizontal** row.
  - `1`, `"vert"`, `"vertical"`: Arrange elements in a **vertical** column.
  - `None`: Elements control their own placement using their `x/y` values.
- **appMessages** *(bool)* - Enables/disables event messages (e.g., resize notifications).
- **resizable** *(bool)* - Allows window resizing if `True`.
- **minWidth/minHeight** *(int)* - Minimum window size when resizing.
- **maxWidth/maxHeight** *(int)* - Maximum window size when resizing.
  - *Note:* Min/max size only applies when resizing. If the initial size exceeds the limit, it remains unchanged until resized manually.

### Methods

- **addElements(*elements)** - Adds one or more GUI elements (e.g., buttons) to the window.

#### Example:
```python
button1 = Button(text="Click Me", x=50, y=50, width=100, height=50)
window.addElements(button1)
```

---

## Button

The **Button** module creates interactive buttons with various customization options.

### Attributes

- **width / height** *(int)* - Button size.
- **x / y** *(int)* - Button position.
- **text** *(str)* - Displayed text (centered by default).
- **id** *(any, default: None)* - Unique identifier for function mapping.
- **content** *(any)* - Custom data returned on click.
- **zIndex** *(int, default: 0)* - Stack order (higher values render above lower ones).

#### Styling

- **borderWidth** *(int, default: 1)* - Border thickness.
- **borderRadius** *(int, default: 0)* - Corner roundness.
- **clickSink** *(int, default: 1)* - Button depression depth on click.
- **backgroundColor** *(RGB, default: blue)* - Button color.
- **textColor** *(RGB, default: black)* - Text color.
- **borderColor** *(RGB, default: black)* - Border color.
- **hoverColor** *(RGB)* - Color when hovered.
- **clickColor** *(RGB)* - Color when clicked.
- **textHoverColor** *(RGB, default: None)* - Text color on hover.
- **borderHoverColor** *(RGB)* - Border color on hover.

#### Text Formatting

- **font** *(str, default: Arial)* - Font type.
- **fontSize** *(int, default: 20)* - Font size.
- **capitalize** *(bool)* - Capitalizes each word if `True`.
- **toLowerCase** *(bool)* - Converts text to lowercase.
- **toUpperCase** *(bool)* - Converts text to uppercase.
- **underline** *(bool)* - Underlines text if `True`.

### Methods

- **setText(new_text)** - Updates button text dynamically and re-renders it with transformations.

#### Example:
```python
button1 = Button(text="Old Text")
button1.setText("New Text")
```
This updates the button text dynamically without requiring a full reinitialization.

---

## Summary

Churchred's GUI library simplifies GUI development in Pygame, allowing for easy creation and management of windows and buttons. With intuitive settings and customization options, developers can quickly design functional and interactive interfaces.

