from PIL import Image
import numpy as np
import sys

""" This function splits an image n times in an specific axis """
def split(photo_path, n=2, split_axis="x", input_folder="input/", output_folder="output/"):
    # Open the image
    img = Image.open(f"{input_folder}{photo_path}")
    img_as_array = np.asarray(img)

    # Get the shape of the array representing the img
    y, x, _ = img_as_array.shape

    # Split the img n times in the corresponding axis
    if split_axis == "x":
        sub_img_arrays = [img_as_array[:, i * (x // n) : (i + 1) * (x // n) + 1, :] for i in range(n)]
    else:
        sub_img_arrays = [img_as_array[i * (y // n) : (i + 1) * (y // n) + 1, :, :] for i in range(n)]

    # Generator with the arrays as imgs and save every img
    new_imgs = (Image.fromarray(sub_array, mode=None) for sub_array in sub_img_arrays)
    for index, new_img in enumerate(new_imgs):
        new_img.save(f"{output_folder}{index}.jpg", format='jpeg')

if __name__ == "__main__":
    input_img_name, n = "sunsetcoron4.jpg", 3
    split(input_img_name, n)