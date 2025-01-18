import noise
from PIL import Image

shape = (128, 128)

# composant de la seed
scale = 20.0
octaves = 2
lacunarity = 2.0
persistence = 1.2

blue = (66, 110, 225)
green = (36, 135, 32)
beach = (240, 210, 172)
mountains = (140, 140, 140)
snow = (250, 250, 250)


image_filpath = "map_V2.png"

image = Image.new(mode="RGB", size=shape)

def set_color(x, y, image, value):
    if value < -0.07:
        image.putpixel((x, y), blue)
    elif value < 0:
        image.putpixel((x, y), beach)
    elif value < 0.25:
        image.putpixel((x, y), green)
    elif value < 0.5:
        image.putpixel((x, y), mountains)
    elif value < 1.0:
        image.putpixel((x, y), snow)

for x in range(shape[0]):
    for y in range(shape[1]):
        value = noise.pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=shape[0], repeaty=shape[1], base=0)
        set_color(x, y, image, value)

image.save (image_filpath)
