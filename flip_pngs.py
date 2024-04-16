from PIL import Image
from matplotlib import cm
import numpy as np
import glob
import shutil


def orientation(path):
    im = Image.open(path)
    I = np.asarray(im)
    v = I.mean(0)
    L = v.shape[0]
    return "L" if v[:(L//3)].mean() < v[(2*L//3):].mean() else "R"

def flip_image(input_image_path, output_image_path, direction='horizontal'):
    image = Image.open(input_image_path)
    if direction == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == 'vertical':
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Invalid direction. Choose 'horizontal' or 'vertical'.")
    
    flipped_image.save(output_image_path)

def process_dir(source, target):
    for path in glob.glob(source + "*.png"):
        o = orientation(path)
        target_path = path.replace(source, target)
        if ("-L-"in path and o =="L") or ("-R-"in path and o =="R"):
            flip_image(path, target_path)
            print(f"Flipped {path}")
        else:
            shutil.copy(path, target_path)
            print(f"Not flipped {path}")
            
    
# Example usage:
# input_image_path = "input.png"
# output_image_path = "output.png"
# flip_image(input_image_path, output_image_path, direction='horizontal')

source = "experiment_data/images/"
target = "experiment_data/images_flipped/"
process_dir(source, target)
