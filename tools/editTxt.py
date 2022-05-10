# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# 获取文件名列表到txt
 
import os
 
img_path = '/home/v4r/Person/CKH/dataset/fastener/test/images_200/multi'
img_list=os.listdir(img_path)
print('img_list: ',img_list)
 
with open('val_multi.txt','w') as f:
    for img_name in img_list:
        name = img_name.split('.')[0]
        f.write(name+'\n')