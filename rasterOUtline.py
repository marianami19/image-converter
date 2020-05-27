from matplotlib.pyplot import imread
from scipy import misc

fimg = imread('/home/althea/PycharmProjects/College/Konverze.png');
from skimage import color

gimg = color.colorconv.rgb2grey(fimg)
from skimage import measure

contours = measure.find_contours(gimg, 0.8)
import matplotlib.pyplot as plt
# import Image

for n, contour in enumerate(contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)

from skimage.draw import ellipse
from skimage.measure import find_contours, approximate_polygon, subdivide_polygon

contour = contours[0]
new_s = contour.copy()
appr_s = approximate_polygon(new_s, tolerance=0.8)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 4))
ax2.plot(contour[:, 0], contour[:, 1])
ax1.plot(appr_s[:, 0], appr_s[:, 1])
plt.show()

