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
                 dims = {0,1,2},
                 random = False):
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

        self.random = random
        self.init_board()
        self.frame_counter = 0

        # todo: make these two adjustable,
        # fix issue where for low random treshold the board is a load of 0's, 
        # most likely since that's the default?
        self.random_rate = 5

        # high threshold means high probablilty of changing
        self.random_threshold = 0.05


    def init_board(self):
        self.board = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for x in range(0, self.width):
            for y in range(0, self.height):
                if x % 2 == 0:
                    if y % 2 == 0:
                            self.board[x][y] = 0
                    else:
                            self.board[x][y] = 1
                else:
                    if y % 2 == 0:
                            self.board[x][y] = 2
                    else:
                            self.board[x][y] = 3

    def randomize_board(self):
        self.board = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for x in range(0, self.width):
            for y in range(0, self.height):
                if random.uniform(0,1) <= self.random_threshold:
                    self.board[x][y] = random.randint(0,3)

    def draw_grid(self, image):
        # maybe move this somewhere else since it's a bit misrepresentative of function name
        self.randomize_board() if self.random and self.frame_counter % self.random_rate == 0 else None
        self.frame_counter += 1

        self.blackout_dims(image, self.dims)

        for x in range(0, self.width):
            for y in range(0, self.height):
                self.draw(x, y, self.board[x][y], image)


    # used to blackout dims that are not being used
    @staticmethod
    def blackout_dims(image, used_dims):
        # True means to black out, False means to keep
        mask = np.ones(3, dtype=bool)
        mask[list(used_dims)] = False
        image[:, :, mask] = 0


    def draw(self, x, y, value, image):
        if self.shape_type == "square":
            set_cell_square(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)
            # set_cell_white(x, y, image, self.cell_h, self.cell_w)
        elif self.shape_type == "cross":
            set_cell_cross(x, y, image, self.cell_h, self.cell_w, self.dims, self.function)
        elif self.shape_type == "triangle":
            set_cell_triangle(x, y, image, self.cell_h, self.cell_w, self.dims, self.function, value)


    def flip_specified_dim(self, image, dim):
        # making sure that the dim is valid
        if dim >= image.shape[2]:
            raise ValueError(f"dim must be less than {image.shape[2]}, but got {dim}")
        
        if dim in self.dims:
            self.dims.remove(dim)
        else:
            self.dims.add(dim)


    def flip_random(self):
        self.random = not self.random

        # need to check if this is redundant, might be doing this double
        if self.random:
            self.randomize_board()
        else:
            self.init_board()

    def increase_cell_size(self):
        curr_index = self.possible_cell_sizes.index(self.cell_h)

        if curr_index < (len(self.possible_cell_sizes) - 1):
            curr_index += 1
            self.cell_h = self.possible_cell_sizes[curr_index]
            self.cell_w = self.possible_cell_sizes[curr_index]
            self.width = self.frame_width // self.cell_w
            self.height = self.frame_height // self.cell_h

        if self.random:
            self.randomize_board()
        else:
            self.init_board()

    def decrease_cell_size(self):
        curr_index = self.possible_cell_sizes.index(self.cell_h)

        if curr_index > 1:
            curr_index -= 1
            self.cell_h = self.possible_cell_sizes[curr_index]
            self.cell_w = self.possible_cell_sizes[curr_index]
            self.width = self.frame_width // self.cell_w
            self.height = self.frame_height // self.cell_h

        if self.random:
            self.randomize_board()
        else:
            self.init_board()



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

