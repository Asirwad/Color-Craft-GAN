from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt
import os
from tensorflow import keras

batch_size = 64
img_size = 120
dataset_split = 2500

master_dir = "data"
x = []
y = []
for image_file in os.listdir(master_dir)[0 : dataset_split]:
    rgb_image = Image.open(os.path.join(master_dir, image_file)).resize(img_size, img_size)
    # Normalize the RGB image array
    rgb_image_array = (np.asarray(rgb_image))/255
    grey_image = rgb_image.convert('L')
    # Normalize the Grey scale image array
    grey_image_array = (np.asarray(grey_image).reshape((img_size, img_size, 1)))/255
    x.append(grey_image_array)
    y.append(rgb_image_array)

# train test splitting
train_x, test_x , train_y, test_y = train_test_split(np.array(x), np.array(y), test_size=0.1)

# Construct tf.data.Dataset object
dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y))
dataset = dataset.batch(batch_size)
