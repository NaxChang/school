from collections import namedtuple

Color = namedtuple("Color", ["red", "green", "blue"])

color = Color(55, 155, 255)
white = Color(55, 155, 255)

print(color.blue)
