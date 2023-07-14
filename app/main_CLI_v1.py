from tkinter import filedialog
from app.colorize import colorize

print("Color-Craft-GAN CLI")
image_filepath = filedialog.askopenfilename(title='Select grey scale image')
colorized_image_filepath = colorize(image_filepath)
print(f"Colorized image saved at: {colorized_image_filepath}")