import cv2
import random
import numpy as np


def get_common_divisors(x, y):
    result = []

    # determining which one is the bigger num
    smaller = x
    bigger = y

    if x > y:
        smaller = y
        bigger = x

    # start at 1 because dividing through 0 is undefined
    for i in range (1, smaller + 1):
        # so if i is a common divisor
        if (bigger % i == 0) & (smaller % i == 0):
            result.append(i)
    return result

def set_grid_white(x, y, image, cell_hw):
    image[(y * cell_hw):((y + 1 )* cell_hw), (x * cell_hw):((x + 1 )* cell_hw)] = [255, 255, 255]


# Now trying to do mean over each dim
def set_grid_mean(x, y, image, cell_hw, dims = 3):
    # get block boundaries
    row_start = y * cell_hw
    row_end   = (y + 1) * cell_hw
    col_start = x * cell_hw
    col_end   = (x + 1) * cell_hw

    # determine what to modify based on parity
    row_slice = slice(row_start, row_start + cell_hw//2) if y % 2 == 0 else slice(row_start + cell_hw//2, row_end)
    col_slice = slice(col_start, col_start + cell_hw//2) if x % 2 == 0 else slice(col_start + cell_hw//2, col_end)

    for i in range(0, dims):
        image[row_start:row_end, col_start:col_end, i] = np.mean(image[row_start:row_end, col_start:col_end, i])


# Now trying to do max over each dim
# Max behaves unexpectedly
def set_grid_max(x, y, image, cell_hw, dims = 3):
    # get block boundaries
    row_start = y * cell_hw
    row_end   = (y + 1) * cell_hw
    col_start = x * cell_hw
    col_end   = (x + 1) * cell_hw

    # determine what to modify based on parity
    row_slice = slice(row_start, row_start + cell_hw//2) if y % 2 == 0 else slice(row_start + cell_hw//2, row_end)
    col_slice = slice(col_start, col_start + cell_hw//2) if x % 2 == 0 else slice(col_start + cell_hw//2, col_end)

    for i in range(0, dims):
        image[row_start:row_end, col_start:col_end, i] = np.max(image[row_start:row_end, col_start:col_end, i])


# Now trying to do mean over each dim
def set_grid_mean_cross_mask(x, y, image, cell_hw, dims = 3):
    # get block boundaries
    row_start = y * cell_hw
    row_end   = (y + 1) * cell_hw
    col_start = x * cell_hw
    col_end   = (x + 1) * cell_hw

    # change whole grid to mean
    for i in range(0, dims):
        image[row_start:row_end, col_start:col_end, i] = np.mean(image[row_start:row_end, col_start:col_end, i])

    # determine what to part of cell to modify based on parity
    row_slice = slice(row_start, row_start + cell_hw//2) if y % 2 == 0 else slice(row_start + cell_hw//2, row_end)
    col_slice = slice(col_start, col_start + cell_hw//2) if x % 2 == 0 else slice(col_start + cell_hw//2, col_end)

    # modify said part to white
    image[row_slice, col_slice] = [255,255,255]

    
def set_grid_mean_triangle_mask(x, y, image, cell_hw, dims = 3):
    # get block boundaries
    row_start = y * cell_hw
    row_end   = (y + 1) * cell_hw
    col_start = x * cell_hw
    col_end   = (x + 1) * cell_hw

    # change whole grid to mean
    for i in range(0, dims):
        image[row_start:row_end, col_start:col_end, i] = np.mean(image[row_start:row_end, col_start:col_end, i])

    
    if x % 2 == 0:
        if y % 2 == 0:
            for i in range(0, cell_hw):
                image[(y * cell_hw):((y + 1 )* cell_hw - i), col_start + i ] = [255, 255, 255]
        else:
            for i in range(0, cell_hw):
                image[row_start + i :((y + 1 )* cell_hw), col_start + i ] = [255, 255, 255]
    else:
        if y % 2 == 0:
            for i in range(0, cell_hw):
                image[(y * cell_hw):row_start + i, col_start + i ] = [255, 255, 255]
        else:
            for i in range(0, cell_hw):
                image[row_start + i :((y + 1 )* cell_hw), (col_end - i - 1) ] = [255, 255, 255]


def set_grid_mean_rand_triangle_mask(x, y, image, cell_hw, dims = 3):
    # get block boundaries
    row_start = y * cell_hw
    row_end   = (y + 1) * cell_hw
    col_start = x * cell_hw
    col_end   = (x + 1) * cell_hw

    # change whole grid to mean
    for i in range(0, dims):
        image[row_start:row_end, col_start:col_end, i] = np.mean(image[row_start:row_end, col_start:col_end, i])

    rand = random.choice([0, 1, 2, 3])
    
    if rand == 0:
        for i in range(0, cell_hw):
            image[(y * cell_hw):((y + 1 )* cell_hw - i), col_start + i ] = [255, 255, 255]
    elif rand == 1:
        for i in range(0, cell_hw):
            image[row_start + i :((y + 1 )* cell_hw), col_start + i ] = [255, 255, 255]
    elif rand == 2:
        for i in range(0, cell_hw):
            image[(y * cell_hw):row_start + i, col_start + i ] = [255, 255, 255]
    else:
        for i in range(0, cell_hw):
            image[row_start + i :((y + 1 )* cell_hw), (col_end - i - 1) ] = [255, 255, 255]