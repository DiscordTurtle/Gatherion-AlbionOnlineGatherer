import os
import random
import shutil

input_folder = './input_pictures/input_stone'
fileList = os.listdir(input_folder)

# Extracting only image files
imgList = [file for file in fileList if file.endswith('.jpg')]

# Shuffling images
random.shuffle(imgList)

split = 0.2

train_path = 'models/data/train'
val_path = 'models/data/val'

images_train_path = os.path.join(train_path, 'images')
labels_train_path = os.path.join(train_path, 'labels')

images_val_path = os.path.join(val_path, 'images')
labels_val_path = os.path.join(val_path, 'labels')

# Function to empty a directory
def empty_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

empty_directory(images_train_path)
empty_directory(labels_train_path)
empty_directory(images_val_path)
empty_directory(labels_val_path)

# imgLen = len(imgList)
# print("Images in total: ", imgLen)

# split_index = int(imgLen * (1 - split))

# train_images = imgList[:split_index]
# val_images = imgList[split_index:]
# print("Training images: ", len(train_images))
# print("Validation images: ", len(val_images))

# for imgName in train_images:
#     og_path = os.path.join(input_folder, imgName)
#     target_path = os.path.join(images_train_path, imgName)

#     shutil.copyfile(og_path, target_path)

#     og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
#     target_txt_path = os.path.join(labels_train_path, imgName.replace('.jpg', '.txt'))

#     shutil.copyfile(og_txt_path, target_txt_path)

# for imgName in val_images:
#     og_path = os.path.join(input_folder, imgName)
#     target_path = os.path.join(images_val_path, imgName)

#     shutil.copyfile(og_path, target_path)

#     og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
#     target_txt_path = os.path.join(labels_val_path, imgName.replace('.jpg', '.txt'))

#     shutil.copyfile(og_txt_path, target_txt_path)

# print("Done!")
