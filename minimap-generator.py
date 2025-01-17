import noise
from PIL import Image

shape = (128, 128)

scale = 25.0
octaves = 2
lacunarity = 2.0
persistence = 1.2

image_filpath = "map.png"

image = Image.new(mode="RGB", size=shape)

for x in range(shape[0]):
    for y in range(shape[1]):
        value = noise.pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=shape[0], repeaty=shape[1], base=0)
        image.putpixel((x, y), (int(value*255), int(value*255), int(value*255)))

image.save (image_filpath)