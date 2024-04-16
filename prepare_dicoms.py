import pydicom as dicom
import png
import pydicom
import os
import glob

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

dirpath = "/home/aikopernik/workspace/mammography_metarepository/experiment_data/images/"
def generate_path(filepath):
    ds = dicom.read_file(filepath)
    group_id = filepath.split("/")[-4]
    study_id = filepath.split("/")[-3]
    path = group_id + "-" + study_id + "-" + ds[(0x0008, 0x103e)].value.replace(" ", "-") + ".png"

    if os.path.exists(dirpath + path):
        return
    try:
        save_dicom_image_as_png(filepath, dirpath + path)
    except:
        print("Read error")
        return

test = "/media/aikopernik/EBC6-BD83/DICOM/DICOM_PACZKA_1/1.2.826.0.1.3680043.2.135.736037.776827.7.1712922077.500.32/20200922/1.2.826.0.1.3680043.2.135.736037.776827.7.1712922079.937.37.dcm"

paths = glob.glob("/media/aikopernik/EBC6-BD83/DICOM/**/*.dcm", recursive=True)
for path in paths:
    print(path)
    print(generate_path(path))
