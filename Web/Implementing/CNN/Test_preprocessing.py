from PIL import Image
import os

def turn_to_RGB(dataset, number):
    num = str(number)
    path_dir = dataset + '/' + num
    file_list = os.listdir(path_dir)
    for i, j in enumerate(file_list):
        real_dir = dataset + '/' + num + '/' + file_list[i]
        img = Image.open(real_dir).convert('RGB')
        img.save(real_dir)
        resize_image = Image.open(real_dir).resize((100, 100))
        resize_image.save(real_dir)

def main():
    for i in range(10):
        turn_to_RGB('CNN/predict', i)
