# JPG to PNG Converter
import sys
import os
from PIL import Image, ImageFilter

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new/ exists, if not create /new dir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex,
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # split extension to save as png
    clean_name = os.path.splitext(filename)[0]
    # convert images to png
    # save to the new folder
    img.save(f'{output_folder}{clean_name}.png', 'PNG')
    print("All Done!!")