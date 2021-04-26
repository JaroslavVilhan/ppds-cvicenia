from numba import cuda
import cv2
from PIL import Image


@cuda.jit
def my_kernel(data, out):
    """
    prevedie obrazok na odtiene sivej

    vypocet podla:
    http://harmanani.github.io/classes/csc447/Notes/Lecture16.pdf
    """

    x, y = cuda.grid(2)  # pozicia aktualneho vlakna v mriezke

    # grayscale weights: 0.21*r, 0.71*g, 0.07*b
    out[x][y] = 0.21*data[x][y][0] + 0.71*data[x][y][1] + 0.07*data[x][y][2]


img = cv2.imread('img.jpg')
rows, cols, colors = img.shape

# Copy to the device
input_data = cuda.to_device(img)

# Allocate memory on the device for the result
global_mem = cuda.device_array((rows, cols))

threadsperblock = (32, 32)

blockspergrid_x = (rows + (threadsperblock[0] - 1)) // threadsperblock[0]
blockspergrid_y = (cols + (threadsperblock[1] - 1)) // threadsperblock[1]
blockspergrid = (blockspergrid_x, blockspergrid_y)

my_kernel[blockspergrid, threadsperblock](input_data, global_mem)

# copy the result back to the host
res = global_mem.copy_to_host()

img = Image.fromarray(res)
img = img.convert('RGB')
img.save('out.jpg')
