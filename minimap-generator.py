from PIL import Image
import noise

# Function that asks the user for a 12-digit seed
def get_seed():
    while True:
        seed = input("Enter a 12-digit seed (example: 123456789012): ")

        # Check if the seed is 12 digits
        if len(seed) == 12 and seed.isdigit():
            return seed
        else:
            print("The seed must be exactly 12 digits. Please try again.")
            
def get_shapeX():
    shapeX = int(input("Enter the value for your map (length): "))
    return shapeX

def get_shapeY():
    shapeY = int(input("Enter the value for your map (width): "))
    return shapeY

# Determine the color based on the noise value
def set_color(x, y, image, value):
    blue = (66, 110, 225)
    green = (36, 135, 32)
    beach = (240, 210, 172)
    mountains = (140, 140, 140)
    snow = (250, 250, 250)
    
    if value < -0.07:
        image.putpixel((x, y), blue)
    elif value < 0:
        image.putpixel((x, y), beach)
    elif value < 0.25:
        image.putpixel((x, y), green)
    elif value < 0.5:
        image.putpixel((x, y), mountains)
    else:
        image.putpixel((x, y), snow)

# Main function to generate the map
def generate_map():
    # Get the seed and shape entered by the user
    seed = get_seed()
    
    # In french we said "c'est ghetto mais ça fonctionne"
    shapeX = get_shapeX()
    shapeY = get_shapeY()
    shape = [shapeX, shapeY]

    # Generation parameters based on the seed
    scale = int(seed[:3]) / 10 # Noise scale
    octaves = int(seed[3:6]) // 100 # Number of octaves for complexity
    lacunarity = int(seed[6:9]) / 10  # Lacunarity to control detail variation
    persistence = int(seed[9:12]) / 10 # Persistence to control noise attenuation
    shape = (shapeX, shapeY)  # Map size (width x height)
    image = Image.new(mode="RGB", size=shape)
    for x in range(shape[0]):
        for y in range(shape[1]):
            value = noise.pnoise2(
                x / scale, 
                y / scale, 
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=shape[0],
                repeaty=shape[1],
                base=0
            )
            set_color(x, y, image, value)
    image_filepath = "map.png"
    image.save(image_filepath)
    print(f"Map generated and saved as: {image_filepath}")
    image.show()

# Call the main function to generate the map
if __name__ == "__main__":
    generate_map()
