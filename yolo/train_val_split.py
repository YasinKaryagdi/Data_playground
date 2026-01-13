import numpy as np
import os
from pathlib import Path
import argparse
import random
import shutil


def split(data_path,
        train_percent = 0.8): 

    print(f"testing input path: {data_path}")
    # Get path to input dataset based of dataset
    # (may differ for each project)
    input_image_path = os.path.join(data_path,'images')
    input_label_path = os.path.join(data_path,'annotations')
    print(f"testing input path: {input_image_path}")
    print(f"testing input path: {input_label_path}")

    # init paths to image and annotation folders
    cwd = os.getcwd()
    train_img_path = os.path.join(cwd,'data/train/images')
    train_txt_path = os.path.join(cwd,'data/train/labels')
    val_img_path = os.path.join(cwd,'data/validation/images')
    val_txt_path = os.path.join(cwd,'data/validation/labels')


    # create folders if they don't already exist
    for dir_path in [train_img_path, train_txt_path, val_img_path, val_txt_path]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f'Created folder at {dir_path}.')


    # get list of all images and annotation files
    img_file_list = [path for path in Path(input_image_path).rglob('*')]
    txt_file_list = [path for path in Path(input_label_path).rglob('*')]

    print(f'Number of image files: {len(img_file_list)}')
    print(f'Number of annotation files: {len(txt_file_list)}')

    # Determine number of files to move to each folder
    file_num = len(img_file_list)
    train_num = int(file_num*train_percent)
    val_num = file_num - train_num
    print('Images moving to train: %d' % train_num)
    print('Images moving to validation: %d' % val_num)

    # select files to go in train and copy them over
    for i in range(train_num):
        # get random file, make it curr file
        img_path = random.choice(img_file_list)
        img_fn = img_path.name
        base_fn = img_path.stem
        txt_fn = base_fn + '.txt'
        txt_path = os.path.join(input_label_path,txt_fn)

        # Copy first set of files to train folders
        new_img_path, new_txt_path = train_img_path, train_txt_path

        shutil.copy(img_path, os.path.join(new_img_path,img_fn))
        if os.path.exists(txt_path): # If txt path does not exist, this is a background image, so skip txt file
            shutil.copy(txt_path,os.path.join(new_txt_path,txt_fn))

        # remove curr file as an option to pick from
        img_file_list.remove(img_path)

    # sanity check
    train_img_file_list = [path for path in Path(train_img_path).rglob('*')]
    train_txt_file_list = [path for path in Path(train_txt_path).rglob('*')]

    print(f'Number of image files in train folder: {len(train_img_file_list)}')
    print(f'Number of annotation files in train folder: {len(train_txt_file_list)}')

    # select files to go in validate and copy them over
    for i in range(val_num):
        # get random file, make it curr file
        img_path = random.choice(img_file_list)
        img_fn = img_path.name
        base_fn = img_path.stem
        txt_fn = base_fn + '.txt'
        txt_path = os.path.join(input_label_path,txt_fn)

        # Copy first set of files to train folders
        new_img_path, new_txt_path = val_img_path, val_txt_path

        shutil.copy(img_path, os.path.join(new_img_path,img_fn))
        if os.path.exists(txt_path): # If txt path does not exist, this is a background image, so skip txt file
            shutil.copy(txt_path,os.path.join(new_txt_path,txt_fn))

        # remove curr file as an option to pick from
        img_file_list.remove(img_path)

    # sanity check
    val_img_file_list = [path for path in Path(val_img_path).rglob('*')]
    val_txt_file_list = [path for path in Path(val_txt_path).rglob('*')]

    print(f'Number of image files in val folder: {len(val_img_file_list)}')
    print(f'Number of annotation files in val folder: {len(val_txt_file_list)}')


def parse_opt():
    parser = argparse.ArgumentParser()

    # Define and parse user input arguments
    parser.add_argument('--train_percent', 
                        help='Used to specify what test-val split you want,' \
                        'this will be the amount that goes into test',
                        default= 0.8)
    parser.add_argument('--data_path', 
                        help='Path to data folder containing images and annotations',
                        default= "raw_data")
    
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()

    
    print("this opt is:", opt)
    split(**vars(opt))