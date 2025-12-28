import cv2
import argparse
from helper_functions import *
from grid import Grid_Square

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


    # starts with biggest possible cell size
    grid = Grid_Square(frame_width, frame_height, shape_type=shape, dims=[0,1,2])

    while True:
        ret, frame = cam.read()

        # making changes to the frame
        for x in range(0, grid.width):
            for y in range(0, grid.height):
                grid.draw(x, y, frame)


        # write the frame to the output file
        if(save):
            out.write(frame)

        # display the captured frame
        cv2.imshow('Camera', frame)

        
        # if nothing is pressed skips the rest of the loop,
        # ensures that the video feed doesn't suffer too much from these checks
        pressed_key = cv2.waitKey(1)
        if pressed_key == -1:
            continue

        # press 'q' to exit the loop,
        # press 'n' or 'm' to change cell size,
        # press 'l' or 'k' to change function type,
        # press 'o' or 'p' to change filter type,
        if pressed_key == ord('q'):
            break
        elif pressed_key == ord('n'):
            grid.decrease_cell_size()
        elif pressed_key == ord('m'):
            grid.increase_cell_size()
        elif pressed_key == ord('k'):
            grid.change_funct_down()
        elif pressed_key == ord('l'):
            grid.change_funct_up()
        elif pressed_key == ord('o'):
            grid.change_filter_down()
        elif pressed_key == ord('p'):
            grid.change_filter_up()

    # Release the capture and writer objects
    cam.release()
    if(save):
        out.release()
    cv2.destroyAllWindows()


def parse_opt():
    #todo: need to go through these later
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