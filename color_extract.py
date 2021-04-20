# =====This part is using colorgram to extract colors from the image. ====#
import colorgram

colors = colorgram.extract("brighter_dots.jpg", 60)

color_list = []
for color in colors:
    new_color = color.rgb
    r = new_color[0]
    g = new_color[1]
    b = new_color[2]
    color_list.append((r, g, b))

print(color_list)
