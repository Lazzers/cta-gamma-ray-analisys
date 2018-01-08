from astropy.wcs import WCS
import numpy as np


class BlobResult:

	def __init__(self, fits_path):
		"""
		Constructor
		"""
		self.path_map = fits_path
		self.bary = None
		self.diam = None
		self.radius = None
		self.radec = None
		self.mask = None
		return

	def set_bary(self, barycenter):
		self.bary = barycenter
		wcs = WCS(self.path_map)
		ra, dec = wcs.wcs_pix2world(self.bary[0], self.bary[1], 0)
		self.radec = [ra, dec]
		return

	def set_diameter(self, size):
		self.diam = size
		self.radius = size/2
		return

	def set_mask(self, shape):
		msk = np.zeros(shape)
		ykp = int(self.bary[0])  # why?
		xkp = int(self.bary[1])
		for i in range(-int(self.radius), int(self.radius)):
			for j in range(-int(self.radius), int(self.radius)):
				msk[xkp + i, ykp + j] = 1
		self.mask = msk.astype(np.uint8)
		return

	def print_values(self):
		print("Barycenter: ({0}, {1})".format(np.round(self.bary[0],2),np.round(self.bary[1],2)))
		print("Radius: {0}".format(np.round(self.radius, 3)))
		print("RA,Dec: ({0}, {1})".format(np.round(self.radec[0], 3), np.round(self.radec[1], 3)))
		return
