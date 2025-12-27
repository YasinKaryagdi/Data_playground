import cv2
import argparse
from helper_functions import *

def run(save = False,
        name = "output",
        shape = "triangle",
        random = False):  
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the codec and create VideoWriter object
    if(save):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f'{name}.mp4', fourcc, 20.0, (frame_width, frame_height))

    # stores all possible cell sizes,
    # current cell is stored as index i
    cell_size = get_common_divisors(frame_width, frame_height)

    # starts with biggest possible
    i = len(cell_size) - 1
    while True:
        ret, frame = cam.read()

        # making changes to the frame
        for x in range(0, frame_width // cell_size[i]) :
            for y in range(0, frame_height // cell_size[i]):
                set_grid_mean_rand_triangle_mask(x, y, frame, cell_size[i])


        # write the frame to the output file
        if(save):
            out.write(frame)

        # display the captured frame
        cv2.imshow('Camera', frame)

        # press 'q' to exit the loop,
        # press 'm' to increase cell size,
        # press 'n' to decrease cell size
        pressed_key = cv2.waitKey(1)
        if pressed_key == ord('q'):
            break
        elif pressed_key == ord('m'):
            # making sure it doesn't go out of bound
            if i < (len(cell_size) - 1):
                i += 1
        elif pressed_key == ord('n'):
            if i > 1:
                i -= 1

    # Release the capture and writer objects
    cam.release()
    if(save):
        out.release()
    cv2.destroyAllWindows()


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", help="do not save images/videos")
    parser.add_argument("--name", default="output", help="save results to project/name")

    parser.add_argument("--shape", default="triangle", help="starting shape")
    parser.add_argument("--random", action="store_true", help="decides whether shapes dynamically change")
    # TODO: add a "random speed", 
    # which essentially determines how fast the shapes change (in frames)
    
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()

    
    print("this opt is:", opt)
    run(**vars(opt))