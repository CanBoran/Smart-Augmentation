import os


for file in os.listdir('./landscape/'):
    res = os.popen("identify './landscape/" + str(file) + "' | awk ' {print $3} '").read()
    dim = res.split("x")

    x_dim = int(dim[0]) 
    y_dim = int(dim[1])

    if (x_dim < 256) or (y_dim < 256 ):
        continue

    if x_dim > y_dim:
	crop_dim = round((y_dim*3)/4)
	x_offset = x_dim-crop_dim
	y_offset = y_dim-crop_dim

	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+0+0 './landscape_cropped/cropped_" + str(file) + "_1'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(round(x_offset/2)) + "+0 './landscape_cropped/cropped_" + str(file) + "_2'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(x_offset) + "+0 './landscape_cropped/cropped_" + str(file) + "_3'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+0+" + str(y_offset) + " './landscape_cropped/cropped_" + str(file) + "_4'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(round(x_offset/2)) + "+0+" + str(y_offset) + " './landscape_cropped/cropped_" + str(file) + "_5'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(x_offset) + "+" + str(y_offset) + " './landscape_cropped/cropped_" + str(file) + "_6'")

    else:
        crop_dim = round((x_dim*3)/4)
	x_offset = x_dim-crop_dim
	y_offset = y_dim-crop_dim

	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+0+0 './landscape_cropped/cropped_" + str(file) + "_1'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+0+" + str(round(y_offset/2)) + " './landscape_cropped/cropped_" + str(file) + "_2'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+0+" + str(y_offset) + " './landscape_cropped/cropped_" + str(file) + "_3'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(x_offset) + "+" + str(round(y_offset/2)) + " './landscape_cropped/cropped_" + str(file) + "_4'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(x_offset) + "+0 './landscape_cropped/cropped_" + str(file) + "_5'")
	os.system("convert './landscape/" + str(file) + "' -crop " + str(crop_dim) + "x" + str(crop_dim) + "+" + str(x_offset) + "+" + str(y_offset) + " './landscape_cropped/cropped_" + str(file) + "_6'")
