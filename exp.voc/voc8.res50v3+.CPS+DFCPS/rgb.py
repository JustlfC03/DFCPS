from PIL import Image
import os
from tqdm import tqdm
import numpy as np

def calculate_rgb_mean(dataset_path):
    total_r, total_g, total_b = 0, 0, 0
    num_images = 0
    lr = []
    lg = []
    lb = []

    
    i=0
    # 遍历数据集中的所有图像
    for root, _, files in os.walk(dataset_path):

        for file in tqdm(files, desc="Calculating RGB mean"):
            #print(i)
            i+=1
            if file.endswith(".jpg") or file.endswith(".png"):
                num_images += 1
                image_path = os.path.join(root, file)

                # 加载图像
                image = Image.open(image_path).convert("RGB")
                width, height = image.size

                # 遍历图像的所有像素并累加RGB值
                for y in range(height):
                    for x in range(width):
                        r, g, b = image.getpixel((x, y))
                        lr.append(r/255)
                        lg.append(g/255)
                        lb.append(b/255)
                        total_r += r/255
                        total_g += g/255
                        total_b += b/255

    # 计算RGB均值
    avg_r = total_r / (num_images * width * height)
    avg_g = total_g / (num_images * width * height)
    avg_b = total_b / (num_images * width * height)

    print(np.mean(lr),np.mean(lg),np.mean(lb))
    print(np.std(lr),np.std(lg),np.std(lb))

    return avg_r, avg_g, avg_b

# 调用函数计算RGB均值
dataset_path = "/home/CYF/TorchSemiSeg-main/DFCPS/DATA/Kvasir/train_aug/image"  # 将此处替换为你的数据集路径
avg_r, avg_g, avg_b = calculate_rgb_mean(dataset_path)
print("RGB均值：")
print("R: {:.2f}".format(avg_r))
print("G: {:.2f}".format(avg_g))
print("B: {:.2f}".format(avg_b))
