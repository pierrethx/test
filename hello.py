import numpy as np
import matplotlib.pyplot as plt

#this imports the example images
from astropy.utils.data import download_file

from astropy.io import fits
#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
image_file="/Users/pierre/Downloads/image.J024815-081723_icubes.wc.c5008_29.fits"


hdu_list = fits.open(image_file)
#hdu_list.info()

image_data = hdu_list[0].data
hdu_list.close()
#print(type(image_data))
#print(image_data.shape)
image_file2="/Users/pierre/Downloads/image.J024815-081723_icubes.wc.c5008_29_VAR.fits"


hdu_list2 = fits.open(image_file2)
#hdu_list.info()

image_data2 = hdu_list2[0].data
#print(type(image_data))
#print(image_data.shape)
hdu_list2.close()

sigtonoise=image_data/image_data2
fig, ax=plt.subplots()

#star=ax[0].imshow(image_data, cmap='bone')
#noise=ax[1].imshow(image_data2, cmap='pink')
ston=ax.imshow(sigtonoise, cmap='Wistia')
plt.colorbar(ston)
plt.show()

print("Hewwo owo")
