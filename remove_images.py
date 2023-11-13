import os

image_path = 'data/images/train'
label_path = 'data/labels/train'

# List all files in the image and label directories
image_files = os.listdir(image_path)
label_files = os.listdir(label_path)

# Get the base names (without extensions) of image and label files
image_names = [os.path.splitext(file)[0] for file in image_files]
label_names = [os.path.splitext(file)[0] for file in label_files]

# Find images without corresponding labels
images_to_remove = [image for image in image_names if image not in label_names]

# Remove the images without labels
for image in images_to_remove:
    image_file = os.path.join(image_path, image)
    os.remove(image_file)

print(f"Removed {len(images_to_remove)} images.")
