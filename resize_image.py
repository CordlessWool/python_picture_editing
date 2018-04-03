from PIL import Image
import sys, getopt
import os
import re

path = sys.argv[1]

for (dirpath, dirname, filenames) in os.walk(path):
	break

for filename in filenames:
	if re.match(r'[\w ()-\[\]]*.(jpg|jpeg|png)', filename):
		image_1 = Image.open(path+filename)
		image_1.thumbnail((1280, 1280))
		image_1.save(path+filename)
		print(image_1.size)


