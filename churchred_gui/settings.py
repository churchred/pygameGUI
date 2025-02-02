import pygame

colorIndex = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),

    "red": (200, 22, 22),
    "redLight": (147, 16, 16),
    "redDark": (229, 102, 102),

    "blue": (32, 79, 208),
    "blueLight": (86, 127, 239),
    "blueDark": (25, 60, 159),

    "green": (33, 174, 17),
    "greenLight": (129, 206, 120),
    "greenDark": (22, 112, 12),

    "yellow": (200, 195, 44),
    "yellowLight": (151, 147, 33),
    "yellowDark": (237, 233, 115),

    "orange": (241, 135, 15),
    "orangeLight": (251, 172, 81),
    "orangeDark": (182, 117, 43),

    "purple": (191, 89, 216),
    "purpleLight": (221, 103, 250),
    "purpleDark": (146, 67, 166),

    "grey": (137, 137, 137),
    "greyLight": (210, 210, 210),
    "greyDark": (82, 82, 82)
}


mouseCursor = {
  "arrow" : pygame.SYSTEM_CURSOR_ARROW,
  "text"  : pygame.SYSTEM_CURSOR_IBEAM,
  "hand"  : pygame.SYSTEM_CURSOR_HAND 
}


directions = [
  [0, "hor", "horizontal"],
  [1, "vert", "vertical"],
]