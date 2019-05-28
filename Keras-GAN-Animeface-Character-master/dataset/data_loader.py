# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:48:11 2018

@author: Duicane
"""

from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
from PIL import Image
import glob
img_dir = 'spiderman'
image_list = []
for filename in glob.glob(img_dir + '\*.png'): #assuming gif
    im=Image.open(filename)
    
    image_rescaled = rescale(im, 1.0 / 4.0, anti_aliasing=False)
    image_list.append(image_rescaled)
