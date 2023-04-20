import colorgram
colors_list = []
colors = colorgram.extract('Modules/Turtle Module/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_list = (r, g, b)
    colors_list.append(new_list)
print(colors_list)
