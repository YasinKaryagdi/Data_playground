import random
import numpy as np

# todo: implement function that sets cell to white, because this is a variant of "set cell square"
# todo: implement other shapes too
# todo: need to make unit tests for these functions (some seem imperfect)
def set_cell_white(x, y, image, cell_h, cell_w):
    image[(y * cell_h):((y + 1 )* cell_h), (x * cell_w):((x + 1 )* cell_w)] = [255, 255, 255]


# Now trying to do mean over each dim
def set_cell_square(x, y, image, cell_h, cell_w, dims, funct = np.mean):
    # get block boundaries
    row_start = y * cell_h
    row_end   = (y + 1) * cell_h
    col_start = x * cell_w
    col_end   = (x + 1) * cell_w


    for i in dims:
        image[row_start:row_end, col_start:col_end, i] = funct(image[row_start:row_end, col_start:col_end, i])


# Now trying to do mean over each dim
def set_cell_cross(x, y, image, cell_h, cell_w, dims, funct = np.mean):
    # get block boundaries
    row_start = y * cell_h
    row_end   = (y + 1) * cell_h
    col_start = x * cell_w
    col_end   = (x + 1) * cell_w

    # change whole cell to funct
    for i in dims:
        image[row_start:row_end, col_start:col_end, i] = funct(image[row_start:row_end, col_start:col_end, i])

    # determine what to part of cell to modify based on parity
    row_slice = slice(row_start, row_start + cell_h//2) if y % 2 == 0 else slice(row_start + cell_h//2, row_end)
    col_slice = slice(col_start, col_start + cell_w//2) if x % 2 == 0 else slice(col_start + cell_w//2, col_end)
    # modify said part to white
    image[row_slice, col_slice] = [255,255,255]


def set_cell_triangle(x, y, image, cell_h, cell_w, dims, funct = np.mean):
    # get block boundaries
    row_start = y * cell_h
    row_end   = (y + 1) * cell_h
    col_start = x * cell_w
    col_end   = (x + 1) * cell_w

    # change whole cell to funct
    for i in dims:
        image[row_start:row_end, col_start:col_end, i] = funct(image[row_start:row_end, col_start:col_end, i])

    
    if x % 2 == 0:
        if y % 2 == 0:
            for i in range(0, cell_h):
                image[(y * cell_h):((y + 1 )* cell_h - i), col_start + i ] = [255, 255, 255]
        else:
            for i in range(0, cell_h):
                image[row_start + i :((y + 1 )* cell_h), col_start + i ] = [255, 255, 255]
    else:
        if y % 2 == 0:
            for i in range(0, cell_h):
                image[(y * cell_h):row_start + i, col_start + i ] = [255, 255, 255]
        else:
            for i in range(0, cell_h):
                image[row_start + i :((y + 1 )* cell_h), (col_end - i - 1) ] = [255, 255, 255]


def set_cell_triangle_rand(x, y, image, cell_h, cell_w, dims, funct = np.mean):
    # get block boundaries
    row_start = y * cell_h
    row_end   = (y + 1) * cell_h
    col_start = x * cell_w
    col_end   = (x + 1) * cell_w

    # change whole cell to funct
    for i in dims:
        image[row_start:row_end, col_start:col_end, i] = funct(image[row_start:row_end, col_start:col_end, i])

    rand = random.choice([0, 1, 2, 3])
    
    if rand == 0:
        for i in range(0, cell_h):
            image[(y * cell_h):((y + 1 )* cell_h - i), col_start + i ] = [255, 255, 255]
    elif rand == 1:
        for i in range(0, cell_h):
            image[row_start + i :((y + 1 )* cell_h), col_start + i ] = [255, 255, 255]
    elif rand == 2:
        for i in range(0, cell_h):
            image[(y * cell_h):row_start + i, col_start + i ] = [255, 255, 255]
    else:
        for i in range(0, cell_h):
            image[row_start + i :((y + 1 )* cell_h), (col_end - i - 1) ] = [255, 255, 255]

