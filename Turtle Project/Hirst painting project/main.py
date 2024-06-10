import colorgram

colors = colorgram.extract('image_spot_painting.jpg', 30)

rgb_colors = []

for colors in colors:
    red = colors.rgb.r
    green = colors.rgb.g
    blue = colors.rgb.b
    rgb_colors.append((red, green, blue))

print(rgb_colors)