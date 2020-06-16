import numpy as np
import matplotlib.pyplot as plt

#this imports the example images
from astropy.utils.data import download_file

from astropy.io import fits
#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
image_file="/Users/pierre/Downloads/image.J024815-081723_icubes.wc.c5008_29.fits"


hdu_list = fits.open(image_file)
#hdu_list.info()

signal = hdu_list[0].data[1:-1][1:-1]
hdu_list.close()
#print(type(image_data))
#print(image_data.shape)
image_file2="/Users/pierre/Downloads/image.J024815-081723_icubes.wc.c5008_29_VAR.fits"


hdu_list2 = fits.open(image_file2)
#hdu_list.info()

var = hdu_list2[0].data
std = np.sqrt(var[1:-1][1:-1])
#print(type(image_data))
#print(image_data.shape)
hdu_list2.close()

sigtonoise=signal/(std)
fig, ax=plt.subplots()

#star=ax.contourf(image_data, cmap='cubehelix')
#noise=ax[1].imshow(image_data2, cmap='pink')
'''
ston=ax.imshow(sigtonoise, cmap='cubehelix')
plt.colorbar(ston)
plt.show()'''

ston=ax.imshow(sigtonoise, cmap='cubehelix')
plt.colorbar(ston)
plt.show()

#fig, ax=plt.subplots()
#histogram=ax.hist(image_data.flatten(), 1000, color="peru")
#plt.show()
#outfile='/Users/pierre/Downloads/signaltonoise-image.J024815-081723_icubes.wc.c5008_29.fits'
#hdu = fits.PrimaryHDU(sigtonoise)
#hdu.writeto(outfile, overwrite=True)
