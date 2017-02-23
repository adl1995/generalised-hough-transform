#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from buildRefTable import *
from matchTable import *
from findMaxima import *
import numpy as np

images = ['Input1Ref.png', 'Input2Ref.png']
for img in images:
	refim = imread(img)
	im = imread('Input1.png')

	table = buildRefTable(refim)
	acc = matchTable(im, table)
	val, ridx, cidx = findMaxima(acc)
	# code for drawing bounding-box in accumulator array...

	acc[ridx - 5:ridx + 5, cidx - 5] = val
	acc[ridx - 5:ridx + 5, cidx + 5] = val

	acc[ridx - 5, cidx - 5:cidx + 5] = val
	acc[ridx + 5, cidx - 5:cidx + 5] = val

	plt.figure(1)
	imshow(acc)
	plt.show()

	# code for drawing bounding-box in original image at the found location...

	# find the half-width and height of template
	hheight = np.floor(refim.shape[0] / 2) + 1
	hwidth = np.floor(refim.shape[1] / 2) + 1

	# find coordinates of the box
	rstart = max(ridx - hheight, 1)
	rend = min(ridx + hheight, im.shape[0] - 1)
	cstart = max(cidx - hwidth, 1)
	cend = min(cidx + hwidth, im.shape[1] - 1)

	# draw the box
	im[rstart:rend, cstart] = 255
	im[rstart:rend, cend] = 255

	im[rstart, cstart:cend] = 255
	im[rend, cstart:cend] = 255

	# show the image
	plt.figure(2), imshow(refim)
	plt.figure(3), imshow(im)
	plt.show()