import pygame

colorIndex = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (200, 22, 22),
    "red_light": (147, 16, 16),
    "red_dark": (229, 102, 102),
    "blue": (32, 79, 208),
    "blue_light": (86, 127, 239),
    "blue_dark": (25, 60, 159),
    "green": (33, 174, 17),
    "green_light": (129, 206, 120),
    "green_dark": (22, 112, 12),
    "yellow": (200, 195, 44),
    "yellow_light": (151, 147, 33),
    "yellow_dark": (237, 233, 115),
    "orange": (241, 135, 15),
    "orange_light": (251, 172, 81),
    "orange_dark": (182, 117, 43),
    "grey": (137, 137, 137),
    "grey_light": (210, 210, 210),
    "grey_dark": (82, 82, 82)
}

mouseCursor = {
  "arrow" : pygame.SYSTEM_CURSOR_ARROW,
  "hand"  : pygame.SYSTEM_CURSOR_IBEAM,
  "text"  : pygame.SYSTEM_CURSOR_HAND 
}