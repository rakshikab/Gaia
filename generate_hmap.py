from PIL import Image


def generate_heightmaps(img_path):
    srcimg = Image.open(img_path)
    data = srcimg.getdata()
    width, height = srcimg.size

    iarray = []
    for pixel in data:
        # this assumes pixel is a tuple of RGBA values
        # i.e. pixel = (0, 0, 0, 0)
        # we are using only the red channel for this
        i = pixel[0] * 1.0 / srcimg.decodermaxblock
        iarray.append(i)

    heightmap = []
    for i in xrange(height):
        heightmap.append(iarray[i*width:(i+1)*width-1])

    return heightmap

