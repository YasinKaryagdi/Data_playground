from shapes import *
from helper_functions import *

# todo: implement non square cells, those need to be dynamic, (inheritance?)
# probably has possible cell size based on divisors of height and width separately

# todo: add an "offset" parameter to shift the grid over by some amount (neet to watch out for boundaries)
class Grid_Square:
    def __init__(self, 
                 frame_width, 
                 frame_height, 
                 #temp params that will be set based on i, might be changed later
                 #cell_h = 1, 
                 #cell_w = 1,
                 shape_type = "square",
                 function = np.mean,
                 dims = [0,1,2]):
        #todo: implement switching random on or off for triangle_rand (and other shapes)

        self.possible_cell_sizes = get_common_divisors(frame_width, frame_height)
        curr_index = len(self.possible_cell_sizes) - 1

        self.cell_h = self.possible_cell_sizes[curr_index]
        self.cell_w = self.possible_cell_sizes[curr_index]

        self.frame_width = frame_width
        self.frame_height = frame_height

        # these are essentially the number of cells in each direction,
        # currenttly assuming square cells,
        # also unused right now
        self.width = frame_width // self.cell_w
        self.height = frame_height // self.cell_h



        self.possible_shapes = ["square", "cross", "triangle", "triangle_rand"]
        if shape_type not in self.possible_shapes:
            raise ValueError(f"shape_type must be one of {self.possible_shapes}, but got {shape_type}")
        self.shape_type = shape_type

        self.possible_functions = [np.mean, np.max, np.min]
        if function not in self.possible_functions:
            raise ValueError(f"function must be one of {self.possible_functions}, but got {function}")
        self.function = function

        self.dims = dims
        

    def draw(self, x, y, image):
        if self.shape_type == "square":
            set_cell_square(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)
            # set_cell_white(x, y, image, self.cell_h, self.cell_w)
        elif self.shape_type == "cross":
            set_cell_cross(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)
        elif self.shape_type == "triangle":
            set_cell_triangle(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)
        elif self.shape_type == "triangle_rand":
            set_cell_triangle_rand(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)


    def increase_cell_size(self):
        curr_index = self.possible_cell_sizes.index(self.cell_h)

        if curr_index < (len(self.possible_cell_sizes) - 1):
            curr_index += 1
            self.cell_h = self.possible_cell_sizes[curr_index]
            self.cell_w = self.possible_cell_sizes[curr_index]
            self.width = self.frame_width // self.cell_w
            self.height = self.frame_height // self.cell_h


    def decrease_cell_size(self):
        curr_index = self.possible_cell_sizes.index(self.cell_h)

        if curr_index > 1:
            curr_index -= 1
            self.cell_h = self.possible_cell_sizes[curr_index]
            self.cell_w = self.possible_cell_sizes[curr_index]
            self.width = self.frame_width // self.cell_w
            self.height = self.frame_height // self.cell_h


    # added for quick comparison/testing
    # todo: maybe merge with change_function_up/down
    def change_filter_up(self):
        curr_index = self.possible_shapes.index(self.shape_type)
        new_index = (curr_index + 1) % len(self.possible_shapes)
        self.shape_type = self.possible_shapes[new_index]


    def change_filter_down(self):
        curr_index = self.possible_shapes.index(self.shape_type)
        new_index = (curr_index - 1) % len(self.possible_shapes)
        self.shape_type = self.possible_shapes[new_index]


    def change_funct_up(self):
        curr_index = self.possible_functions.index(self.function)
        new_index = (curr_index + 1) % len(self.possible_functions)
        self.function = self.possible_functions[new_index]


    def change_funct_down(self):
        curr_index = self.possible_functions.index(self.function)
        new_index = (curr_index - 1) % len(self.possible_functions)
        self.function = self.possible_functions[new_index]

