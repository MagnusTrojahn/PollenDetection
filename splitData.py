import os
import shutil
import random
from tqdm import tqdm

# Define paths
train_path_img = "./yolo_pollen_data/images/train/"
train_path_label = "./yolo_pollen_data/labels/train/"
val_path_img = "./yolo_pollen_data/images/val/"
val_path_label = "./yolo_pollen_data/labels/val/"
test_path = "./yolo_pollen_data/test"

def train_test_split(path, neg_path=None, split=0.2):
    print("------ PROCESS STARTED -------")

    files = list(set([name[:-4] for name in os.listdir(path)]))  # removing duplicate names i.e. counting only number of images

    print(f"--- This folder has a total number of {len(files)} images ---")
    random.seed(42)
    random.shuffle(files)

    test_size = int(len(files) * split)
    train_size = len(files) - test_size

    # creating required directories
    os.makedirs(train_path_img, exist_ok=True)
    os.makedirs(train_path_label, exist_ok=True)
    os.makedirs(val_path_img, exist_ok=True)
    os.makedirs(val_path_label, exist_ok=True)

    # Copy images and text files to train folder
    for filex in tqdm(files[:train_size]):
        if filex == 'classes':
            continue
        img_src = os.path.join(path, filex + '.jpg')
        img_dst = os.path.join(train_path_img, filex + '.jpg')
        txt_src = os.path.join(path, filex + '.txt')
        txt_dst = os.path.join(train_path_label, filex + '.txt')
        shutil.copy2(img_src, img_dst)
        shutil.copy2(txt_src, txt_dst)

    print(f"------ Training data created with 80% split {len(files[:train_size])} images -------")

    if neg_path:
        neg_images = list(set([name[:-4] for name in os.listdir(neg_path)]))  # removing duplicate names i.e. counting only number of images
        for filex in tqdm(neg_images):
            shutil.copy2(os.path.join(neg_path, filex + '.jpg'), os.path.join(train_path_img, filex + '.jpg'))

        print(f"------ Total {len(neg_images)} negative images added to the training data -------")

        print(f"------ TOTAL Training data created with {len(files[:train_size]) + len(neg_images)} images -------")

    # Copy images and text files to validation folder
    for filex in tqdm(files[train_size:]):
        if filex == 'classes':
            continue
        img_src = os.path.join(path, filex + '.jpg')
        img_dst = os.path.join(val_path_img, filex + '.jpg')
        txt_src = os.path.join(path, filex + '.txt')
        txt_dst = os.path.join(val_path_label, filex + '.txt')
        shutil.copy2(img_src, img_dst)
        shutil.copy2(txt_src, txt_dst)

    print(f"------ Testing data created with a total of {len(files[train_size:])} images ----------")


    print("------ TASK COMPLETED -------")


# Split the data into train and test using the train_test_split function
train_test_split(r'C:/Users/magnu/Desktop/Pollendetection/data/data')
