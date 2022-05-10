import cv2
import numpy as np
import os
from pathlib import Path
from PIL import Image

# 新建一个图片加噪点的函数
def random_noise(image,noise_num):
    img_noise = cv2.imread(image) # 读取图片
    rows, cols, chn = img_noise.shape
 
    for i in range(noise_num):
        x = np.random.randint(0, rows)#随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255 # 0代表黑色，255代表白色
    return img_noise

def Add_Salt_Noise(image): # 加椒盐噪声
         img_salt = Image.open(image) # 读取图片
         imgarray = np.array(img_salt)
         height,width = imgarray.shape[0], imgarray.shape[1]
         for i in range(height):
             for j in range(width):
                 if np.random.random(1) < 0.05:
                     if np.random.random(1) < 0.3:
                         imgarray[i][j] = 0
                     else:
                         imgarray[i][j] = 255
         img_salt = Image.fromarray(imgarray)
         return img_salt

# 原图片、标签文件路径
img_path = r'/home/v4r/Person/CKH/dataset/fastener/test/images_200/multi/'
save_img_path = r'/home/v4r/Person/CKH/dataset/fastener/test/images_200/multi/'

i=1000 
# 
for img_file in os.listdir(img_path):
    
    # 增加随机噪点
    Noisenum = np.random.randint(1000, 10000)# 生成随机的噪点数
    Noicepic = random_noise(img_path + img_file, Noisenum)# 给图片加噪点 
    new_file = str('%06d' % (int(img_file[-8:-4])+i)) 
    cv2.imwrite(save_img_path + new_file + '.png', Noicepic)  # 保存png文件

    # 加椒盐噪声
    saltimg = Add_Salt_Noise(img_path + img_file)
    new_file = str('%06d' %(int(new_file)+i))
    cv2.imwrite(save_img_path + new_file + '.png', Noicepic)  # 保存png文件

    image = cv2.imread(img_path + img_file)
    
    # 均值模糊
    blurimg = cv2.blur(image, (15, 1))
    new_file = str('%06d' %(int(new_file)+i))
    cv2.imwrite(save_img_path + new_file + '.png', blurimg)  # 保存png文件

    # 中值模糊
    medianimg = cv2.medianBlur(image, 7)
    new_file = str('%06d' %(int(new_file)+i))
    cv2.imwrite(save_img_path + new_file + '.png', medianimg)  # 保存png文件

    # 自定义模糊
    kernel = np.ones([5, 5], np.float32)/25  #用户自定义模糊，下面除以25是防止数值溢出
    customimg = cv2.filter2D(image, -1, kernel)
    new_file = str('%06d' %(int(new_file)+i))
    cv2.imwrite(save_img_path + new_file + '.png', customimg)  # 保存png文件

