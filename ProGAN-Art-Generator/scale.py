import os
import sys

foldername = sys.argv[1]
for file in os.listdir(foldername):
    res = os.popen("identify './" + foldername + "/" + str(file) + "' | awk ' {print $3} '").read()
    dim = res.split("x")

    print(str(file))
    x_dim = int(dim[0]) 
    y_dim = int(dim[1])

    if (x_dim < 256) or (y_dim < 256 ):
        continue

    if x_dim > y_dim:
        os.system("convert './" + foldername + "/" + str(file) + "' -crop " + str(y_dim) + "x" + str(y_dim) + "+" + str(round((x_dim-y_dim)/2)) + "+0 './" + foldername + "_scaled/scaled_" + str(file) + "'")
    else:
        os.system("convert './" + foldername + "/" + str(file) + "' -crop " + str(x_dim) + "x" + str(x_dim) + "+0+" + str(round((y_dim-x_dim)/2)) + " './" + foldername + "_scaled/scaled_" + str(file) + "'")
