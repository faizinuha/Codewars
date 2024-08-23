from PIL import Image

# Load the image
image_path = "/mnt/data/A_Renaissance-style_painting_of_a_Mars_rover,_usin.png"
image = Image.open(image_path)

# Save it to a new location where it can be accessed for download
save_path = "/mnt/data/Renaissance_style_Mars_rover.png"
image.save(save_path)

save_path
