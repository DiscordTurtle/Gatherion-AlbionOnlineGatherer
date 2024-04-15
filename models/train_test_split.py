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

train_path = 'models/train'
val_path = 'models/val'

def empty_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

empty_directory(train_path)
empty_directory(val_path)



# if not os.path.isdir(train_path):
#     os.makedirs(train_path)
# if not os.path.isdir(val_path):
#     os.makedirs(val_path)

# imgLen = len(imgList)
# print("Images in total: ", imgLen)

# split_index = int(imgLen * (1 - split))

# train_images = imgList[:split_index]
# val_images = imgList[split_index:]
# print("Training images: ", len(train_images))
# print("Validation images: ", len(val_images))

# for imgName in train_images:
#     og_path = os.path.join(input_folder, imgName)
#     target_path = os.path.join(train_path, imgName)

#     shutil.copyfile(og_path, target_path)

#     og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
#     target_txt_path = os.path.join(train_path, imgName.replace('.jpg', '.txt'))

#     shutil.copyfile(og_txt_path, target_txt_path)

# for imgName in val_images:
#     og_path = os.path.join(input_folder, imgName)
#     target_path = os.path.join(val_path, imgName)

#     shutil.copyfile(og_path, target_path)

#     og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
#     target_txt_path = os.path.join(val_path, imgName.replace('.jpg', '.txt'))

#     shutil.copyfile(og_txt_path, target_txt_path)

# print("Done!")
