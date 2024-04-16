cp experiment_data/preprocessed_images/nyu_gmic_experiment01_preprocessing/nyu_gmic_experiment01_cropped_images/ miniatures --recursive
mogrify -resize x256 miniatures/*.png
