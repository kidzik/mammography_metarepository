import png
import pydicom
import os

def save_dicom_image_as_png(dicom_filename, png_filename, bitdepth=12):
    """
    Save 12-bit mammogram from dicom as rescaled 16-bit png file.
    :param dicom_filename: path to input dicom file.
    :param png_filename: path to output png file.
    :param bitdepth: bit depth of the input image. Set it to 12 for 12-bit mammograms.
                     Set to 16 for 16-bit mammograms, etc.
                     Make sure you are using correct bitdepth!
    """
    image = pydicom.read_file(dicom_filename).pixel_array
    with open(png_filename, 'wb') as f:
        writer = png.Writer(
            height=image.shape[0],
            width=image.shape[1],
            bitdepth=bitdepth,
            greyscale=True
        )
        writer.write(f, image.tolist())

dir_path = "sample_data/images_dcm"
for img in os.listdir(dir_path):
    fullpath = dir_path + "/" + img
    print(fullpath)
    targetpath = fullpath.replace("/images_dcm/","/images/").replace(".dcm",".png")
    print(targetpath)
    save_dicom_image_as_png(fullpath, targetpath)
