import os
import sys

foldername = sys.argv[1]

for file in os.listdir(foldername):
    os.system("convert './" + foldername + "/" + str(file) + "' -resize 128x128 './" + foldername + "_resized/resized_" + str(file) + "'")
