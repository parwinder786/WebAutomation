import sys
import os
# from PIL import Image
#
# # grab the first and second argument
#
# print(len(sys.argv))
#
# image_folder = sys.argv[1]
# output_folder = sys.argv[2]
#
# print(image_folder, output_folder)
# #check if folder exists, if not create then create
#
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
# # loop through and converts images to png
# for filename in os.listdir(image_folder):
#     img = Image.open(f'{image_folder}{filename}')
#     clean_name = os.path.splitext(filename)
#     print(clean_name)
#     img.save(f'{output_folder}{filename}.png', '_png')
#     print('all done, after the image is processes')
# # save it to new folder



#-------------new code --------------------


import sys
import os
from pathlib import Path
from PIL import Image

main_path = os.getcwd()

image_path = f"{main_path}/Pokedex/"
new_path = f"{main_path}/New/"

Path(new_path).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(image_path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_path}{filename}')
    img.save(f'{new_path}/{clean_name}.png', 'png')
    print('all done!')