import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#from scipy import ndimage

filepath = "gpyopt_img/img"
gim = Image.open(filepath+"-anim.gif")#.convert('RGB')
#gim = ndimage.imread(filepath+"-anim.gif")
#gim = Image.open(filepath+"014.png")
#im = np.asarray(gim.getdata(), dtype=np.uint8)
#im = np.array(gim)
#img = plt.imread(filepath+"-anim.gif")
#plt.imshow(gim) #ok

#print(gim.shape)
#plt.show()
print(gim)