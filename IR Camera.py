# Uses data from adafruit_amg88xx library
# Modified from the adafruit_amg88xx library rpi_thermal_cam.py
# Author: Alinne Romero-Torres

#import libraries
import numpy as np
from PIL import Image as im
from scipy.interpolate import griddata
import math
import os

# set up a grid
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
print(points)
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]
TEMP = 10
COLORDEPTH = 1024

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#insert Arduino Array here!
x = np.array([21.25, 21.50, 21.75, 21.75, 21.75, 21.75, 22.50, 22.25, 
21.75, 21.00, 21.50, 22.00, 22.00, 22.25, 22.25, 22.00, 
22.00, 22.25, 21.75, 22.00, 22.75, 22.25, 22.25, 22.50, 
22.00, 21.25, 22.25, 23.50, 22.75, 22.00, 22.75, 23.25, 
22.25, 21.50, 22.25, 23.25, 22.50, 22.00, 22.50, 22.25, 
22.50, 22.00, 22.50, 22.50, 22.75, 22.75, 22.50, 22.25, 
22.25, 22.25, 21.75, 22.25, 22.50, 22.50, 22.25, 22.50, 
21.75, 21.50, 22.25, 22.25, 22.25, 22.50, 22.00, 22.25])
colors = []
color = 0

#Name of the picture
name = '100'

height = 240
width = 240

displayPixelWidth = width / 30
displayPixelHeight = height / 30

# Setting the array values to pixel values form 0-255
for i in x:
    color = i
    if color<= TEMP*1:   #0-10
        color = 0
        colors.append(color)
    elif color<= TEMP*2: #11-20
        color = int(color*2)
        colors.append(color)
    elif color<= TEMP*2.25: #21-22
        color = int(color*2)
        colors.append(color)
    elif color<= TEMP*2.5: #23-25
        color = int(color*4)
        colors.append(color)
    elif color<= TEMP*30:  #25-30
        color = int(color*8)
        colors.append(color)
    else:   
        color = int(color*8)
        colors.append(color)

#This sets the data in the array to a specififc data type
data = np.array(colors, np.uint8)

#Interpolation with gridatta and saves as an int array
bicubic = griddata(points, data, (grid_x, grid_y), method='cubic')
#print(bicubic)
#print(type(bicubic))
#print(bicubic.shape)
#print(len(bicubic))
bicubic = bicubic.astype(int)

# This is the pathe for where to save the image
# Set the directory to positive or negative here
path = os.path.join(os.path.expanduser('~'), 'Documents', 'imgdetect-utils-master', 'imgdetect-utils-master', 'datasets', 'ir', 'images', 'negative', (name +'.png'))
#print(path)

#Make an image from the array and multiply the values by 255 to make them visible once the image is saved
# You can uncomment image.show to see them here :)
image = im.fromarray(bicubic)
imageFile= im.fromarray(bicubic*255)
imageFile.save(path)
#image.show()
reimage = image.resize((image.size[0]*100, image.size[1]*100), im.NEAREST)
#reimage.show()



