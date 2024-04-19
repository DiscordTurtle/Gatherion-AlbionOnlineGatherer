import os
import random
import shutil

def train_test_split(input_folder='./input_pictures/input_fish', split=0.2, data_path='models/data'):
    # Extracting only image files
    fileList = os.listdir(input_folder)
    imgList = [file for file in fileList if file.endswith('.jpg')]

    # Shuffling images
    random.shuffle(imgList)

    images_train_path = os.path.join(data_path, 'images', 'train')
    labels_train_path = os.path.join(data_path, 'labels', 'train')

    images_val_path = os.path.join(data_path , 'images', 'val')
    labels_val_path = os.path.join(data_path , 'labels', 'val')

    # Function to empty a directory
    def empty_directory(directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

    empty_directory(images_train_path)
    empty_directory(labels_train_path)
    empty_directory(images_val_path)
    empty_directory(labels_val_path)

    imgLen = len(imgList)
    print("Images in total: ", imgLen)

    split_index = int(imgLen * (1 - split))

    train_images = imgList[:split_index]
    val_images = imgList[split_index:]
    print("Training images: ", len(train_images))
    print("Validation images: ", len(val_images))

    for imgName in train_images:
        og_path = os.path.join(input_folder, imgName)
        target_path = os.path.join(images_train_path, imgName)

        shutil.copyfile(og_path, target_path)

        og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
        target_txt_path = os.path.join(labels_train_path, imgName.replace('.jpg', '.txt'))

        shutil.copyfile(og_txt_path, target_txt_path)

    for imgName in val_images:
        og_path = os.path.join(input_folder, imgName)
        target_path = os.path.join(images_val_path, imgName)

        shutil.copyfile(og_path, target_path)

        og_txt_path = os.path.join(input_folder, imgName.replace('.jpg', '.txt'))
        target_txt_path = os.path.join(labels_val_path, imgName.replace('.jpg', '.txt'))

        shutil.copyfile(og_txt_path, target_txt_path)

    print("Done!")

train_test_split()