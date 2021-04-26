from numba import cuda
import cv2


@cuda.jit
def my_kernel(io_array):
    """
    Code for kernel.
    """
    # code here


img = cv2.imread('img.jpg')
rows, cols, colors = img.shape

threadsperblock = (32, 32)

blockspergrid_x = (rows + (threadsperblock[0] - 1)) // threadsperblock[0]
blockspergrid_y = (cols + (threadsperblock[1] - 1)) // threadsperblock[1]
blockspergrid = (blockspergrid_x, blockspergrid_y)

my_kernel[blockspergrid, threadsperblock]()
