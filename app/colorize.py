from tkinter import filedialog

from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model


def colorize(filepath):
    # Load the saved generator model
    generator = load_model('model/final_model.h5')

    # Load and preprocess the grayscale image
    grayscale_image = Image.open(filepath).resize((120, 120)).convert('L')
    grayscale_array = (np.asarray(grayscale_image) / 255).reshape((1, 120, 120, 1))

    # Colorize the grayscale image using the generator model
    colorized_image = generator.predict(grayscale_array)

    # Convert colorized image array to PIL Image
    colorized_pil_image = Image.fromarray((colorized_image[0] * 255).astype('uint8')).resize((120, 120))

    # Save the colorized image
    color_image_filepath = filepath.replace('.jpg', '_colorized.jpg')
    colorized_pil_image.save(color_image_filepath)

    # Return the saved color image filepath
    return color_image_filepath
